from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import ServicesOfflineSerializer, ServicesVideoSerializer, ServicesSerializer
from .models import Services
from .utils import Util
from ..base.permissions import IsAdminOrReadOnly


class ServicesOfflineAPIView(generics.GenericAPIView):
    serializer_class = ServicesOfflineSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        created = Util.send_services_offline_mail(data)
        if created:
            return Response({'result': True}, status=status.HTTP_200_OK)
        else:
            return Response({'result': False, 'email': ['Ошибка отправления']}, status=status.HTTP_404_NOT_FOUND)


class ServicesVideoAPIView(generics.GenericAPIView):
    serializer_class = ServicesVideoSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        created = Util.send_services_video_mail(data)
        if created:
            return Response({'result': True}, status=status.HTTP_200_OK)
        else:
            return Response({'result': False, 'email': ['Ошибка отправления']}, status=status.HTTP_404_NOT_FOUND)


class ServicesListAPIView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (IsAdminOrReadOnly,)
