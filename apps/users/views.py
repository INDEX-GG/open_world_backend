from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.request import Request

from .models import User, Children, EmailCode
from ..base.permissions import IsOwnerProfile
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


class UserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsOwnerProfile,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


class ChildrenViewSet(generics.CreateAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    permission_classes = (IsOwnerProfile,)


class ChildrenItemViewSet(generics.UpdateAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenItemSerializer
    permission_classes = (IsOwnerProfile,)


class VerifyCodeAPIView(GenericAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        verify_serializer = VerifyCodeSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        data = verify_serializer.data
        code = data.get('code')
        email = data.get('email')
        email_for_verification = EmailCode.objects.get(email=email)
        if code == email_for_verification.code:
            return Response({"valid": "Valid code", "email": email}, status=status.HTTP_200_OK)
        else:
            return Response({"invalid": "Invalid code", "email": email}, status=status.HTTP_404_NOT_FOUND)


class EmailForVerificationView(CreateAPIView):
    queryset = EmailCode.objects.all()
    serializer_class = EmailCodeSerializer

    def create(self, request):
        code = Util.generate_code()
        created = EmailCode.objects.create(email=request.data['email'], code=code)
        if created:
            data = request.data
            email = data['email']
            Util.send_verification_mail(email, code)
            return Response({"email": email, 'result': True}, status=status.HTTP_200_OK)
