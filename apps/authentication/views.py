from django.utils import timezone

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.core.exceptions import ObjectDoesNotExist

from .serializers import *
from .utils import Util


class SendCodeAPIView(generics.CreateAPIView):
    # Sends a code to the email for registration
    queryset = EmailCode.objects.all()
    serializer_class = SendCodeSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']

        if User.objects.filter(email=email).exists():
            return Response({'result': False, "email": ['Пользователь с таким email уже существует']},
                            status=status.HTTP_409_CONFLICT)

        if EmailCode.objects.filter(email=email).exists():
            EmailCode.objects.filter(email=email).delete()

        code = Util.generate_code()
        created = EmailCode.objects.create(email=email, code=code)

        if created:
            data = request.data
            email = data['email']
            Util.send_verification_mail(email, code)
            return Response({'result': True}, status=status.HTTP_200_OK)
        else:
            return Response({"result": False, "email": ['Не удалось отправить код']},
                            status=status.HTTP_404_NOT_FOUND)


class ConfirmationCodeAPIView(generics.GenericAPIView):
    # Checking the code sent to the email
    serializer_class = ConfirmationCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        code = data.get('code')
        email = data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({'result': False, "email": ['Пользователь с таким email уже существует']},
                            status=status.HTTP_409_CONFLICT)
        try:
            email_for_verification = EmailCode.objects.get(email=email)
            if code == email_for_verification.code:
                return Response({"result": True}, status=status.HTTP_200_OK)
            else:
                return Response({"result": False, "email": ['Неправильный код']}, status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'result': False}, status=status.HTTP_404_NOT_FOUND)


class UserRegistrationAPIView(generics.GenericAPIView):
    # User registration
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        email = serializer.validated_data.get('email')
        try:
            email_for_verification = EmailCode.objects.get(email=email)
            if code == email_for_verification.code:
                serializer.save()
                email_for_verification.delete()
                return Response({'result': True}, status=status.HTTP_201_CREATED)
            else:
                return Response({'result': False, 'email': ['Неверный код']}, status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'result': False}, status=status.HTTP_404_NOT_FOUND)


class ResetSendCodeAPIView(generics.CreateAPIView):
    # Sending a code to the email to reset password
    serializer_class = ResetSendCodeSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']

        if email == 'contact-center.burarrc@mail.ru':
            return Response({"result": False, "email": ['Не удалось отправить код']},
                            status=status.HTTP_404_NOT_FOUND)

        if User.objects.filter(email=email).exists():
            if ResetEmailCode.objects.filter(email=email).exists():
                ResetEmailCode.objects.filter(email=email).delete()
            code = Util.generate_code()
            created = ResetEmailCode.objects.create(email=email, code=code)
            if created:
                email = request.data['email']
                Util.send_reset_password_mail(email, code)
                return Response({'result': True}, status=status.HTTP_200_OK)
            else:
                return Response({"result": False, "email": ['Не удалось отправить код']},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'result': False, "email": ['Пользователя с таким email не существует']},
                            status=status.HTTP_404_NOT_FOUND)


class ResetConfirmationCodeAPIView(generics.GenericAPIView):
    # Password recovery code confirmation
    serializer_class = ResetConfirmationCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        code = data.get('code')
        email = data.get('email')

        if User.objects.filter(email=email).exists():
            try:
                email_for_reset = ResetEmailCode.objects.get(email=email)
                if code == email_for_reset.code:
                    return Response({"result": True}, status=status.HTTP_200_OK)
                else:
                    return Response({"result": False, "email": ['Неправильный код']}, status=status.HTTP_404_NOT_FOUND)
            except ObjectDoesNotExist:
                return Response({'result': False}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'result': False, "email": ['Пользователя с таким email не существует']},
                            status=status.HTTP_404_NOT_FOUND)


class ResetPasswordAPIView(generics.GenericAPIView):
    # User password recovery
    serializer_class = ResetPasswordSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        email = serializer.validated_data.get('email')
        user = User.objects.get(email=email)
        try:
            email_for_reset = ResetEmailCode.objects.get(email=email)
            if code == email_for_reset.code:
                user.set_password(serializer.validated_data.get('password'))
                user.save()

                # TODO: Check it
                for token in OutstandingToken.objects.filter(user_id=user.id):
                    if token.expires_at > timezone.now():
                        _, _ = BlacklistedToken.objects.get_or_create(token=token)
                email_for_reset.delete()
                return Response({'result': True}, status=status.HTTP_201_CREATED)
            else:
                return Response({'result': False, 'email': ['Неверный код']}, status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'result': False}, status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(generics.GenericAPIView):
    # User account login
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    # User account logout
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
