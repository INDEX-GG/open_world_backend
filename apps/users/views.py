from django.contrib.auth import get_user_model
from rest_framework import generics

from ..base.permissions import IsOwnerProfile
from .serializers import *


class UserDetailsView(generics.RetrieveUpdateAPIView):
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


class ChildrenItemViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenItemSerializer
    permission_classes = (IsOwnerProfile,)
