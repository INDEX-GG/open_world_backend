from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from apps.base.permissions import IsAdminOrReadOnly
from .serializers import VideoSerializer, GamesSerializer
from .models import Video, Games, GamesImages


class VideoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = _query_param = 'page_limit'
    max_page_size = 1000


# AIzaSyDwaOGOtXS5hDA4C787eCIJJb9bPr9eDU4


class VideoViewSet(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = VideoPagination


class GamesPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = _query_param = 'page_limit'
    max_page_size = 1000


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all().order_by('-pk')
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = GamesPagination
