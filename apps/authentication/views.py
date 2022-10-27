from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .utils import Util


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        email = serializer.validated_data.get('email')
        email_for_verification = EmailCode.objects.get(email=email)
        if code == email_for_verification.code:
            serializer.save()
            user_data = serializer.data
            return Response(user_data, status=status.HTTP_201_CREATED)
        else:
            return Response({"invalid": "Invalid code", "email": email}, status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyCodeAPIView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        verify_serializer = VerifyCodeSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        data = verify_serializer.data
        code = data.get('code')
        email = data.get('email')
        email_for_verification = EmailCode.objects.get(email=email)
        if code == email_for_verification.code:
            return Response({"email": email, "result": True}, status=status.HTTP_200_OK)
        else:
            return Response({"email": email, "result": False}, status=status.HTTP_404_NOT_FOUND)


class EmailForVerificationView(generics.CreateAPIView):
    queryset = EmailCode.objects.all()
    serializer_class = EmailCodeSerializer

    def create(self, request):
        code = Util.generate_code()

        email = request.data['email']
        if EmailCode.objects.filter(email=email).exists():
            EmailCode.objects.filter(email=email).delete()

        created = EmailCode.objects.create(email=request.data['email'], code=code)
        # TODO: Проверка отправилось ли письмо
        if User.objects.filter(email=email).exists():
            return Response({"email": email, 'result': False}, status=status.HTTP_409_CONFLICT)
        else:
            if created:
                data = request.data
                email = data['email']
                Util.send_verification_mail(email, code)
                return Response({"email": email, 'result': True}, status=status.HTTP_200_OK)
            else:
                data = request.data
                email = data['email']
                return Response({"email": email, 'result': False}, status=status.HTTP_404_NOT_FOUND)
