from django.contrib.auth import get_user_model
from rest_framework import generics

from apps.base.permissions import IsOwnerProfile
from apps.users.serializers import *


class UserDetailsAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsOwnerProfile,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


class ChildrenAPIView(generics.CreateAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    permission_classes = (IsOwnerProfile,)


class ChildrenItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenItemSerializer
    permission_classes = (IsOwnerProfile,)
