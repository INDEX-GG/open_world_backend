from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .utils import Util


class SendCodeView(generics.CreateAPIView):
    queryset = EmailCode.objects.all()
    serializer_class = SendCodeSerializer

    def create(self, request):
        email_serializer = SendCodeSerializer(data=request.data)
        email_serializer.is_valid(raise_exception=True)

        email = request.data['email']

        if User.objects.filter(email=email).exists():
            return Response({'result': False, "email": ['Пользователь с таким email уже существует.']},
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
    serializer_class = ConfirmationCodeSerializer

    def post(self, request):
        verify_serializer = ConfirmationCodeSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        data = verify_serializer.data
        code = data.get('code')
        email = data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({'result': False, "email": ['Пользователь с таким email уже существует.']},
                            status=status.HTTP_409_CONFLICT)
        try:
            email_for_verification = EmailCode.objects.get(email=email)
            if code == email_for_verification.code:
                return Response({"result": True}, status=status.HTTP_200_OK)
            else:
                return Response({"result": False, "email": ['Неправильный код']}, status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'result': False}, status=status.HTTP_404_NOT_FOUND)


class UserRegistrationView(generics.GenericAPIView):
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


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
