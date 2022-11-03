from rest_framework import serializers, status
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import EmailCode, ResetEmailCode
from ..users.models import User


class SendCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=64)

    class Meta:
        model = EmailCode
        fields = ['email']


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=64)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = EmailCode
        fields = ['email', 'code']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['email', 'password', 'code']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if not email:
            raise serializers.ValidationError('')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.code = ''
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=64)
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = auth.authenticate(email=email, password=password)

        if not user:
            if User.objects.filter(email=email).exists():
                raise AuthenticationFailed({'email': 'Некорректные данные'}, code=status.HTTP_401_UNAUTHORIZED)
            else:
                raise AuthenticationFailed({'email': 'Такого пользователя не существует'},
                                           code=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            raise AuthenticationFailed({'email': 'Аккаунт отключен'}, code=status.HTTP_403_FORBIDDEN)

        return {
            "email": user.email,
            "tokens": user.tokens,
        }


class ResetSendCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=64)

    class Meta:
        model = ResetEmailCode
        fields = ['email']


class ResetConfirmationCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=64)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = ResetEmailCode
        fields = ['email', 'code']


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=64)
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['email', 'password', 'code']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if not email:
            raise serializers.ValidationError('')
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=255)

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('Bad token')
