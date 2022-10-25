from rest_framework import serializers

from .models import User, EmailCode


# class ChildrenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Children
#         fields = '__all__'
#
#
# class UserSerializer(serializers.ModelSerializer):
#     parents_children = ChildrenSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'name', 'lastname', 'patronymic', 'phone', 'parents_children']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')

        if not email:
            raise serializers.ValidationError('The email should be only contain alphanumeric')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCode
        fields = '__all__'
