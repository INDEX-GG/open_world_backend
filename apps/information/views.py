from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from apps.base.permissions import IsAdminOrReadOnly
from .serializers import (
    VideoSerializer, GamesSerializer, ContactsSerializer, AboutSerializer,
    RecommendationsSerializer)
from .models import (
    Video, Games, Contacts, About, Recommendations)


class VideoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = _query_param = 'page_limit'
    max_page_size = 1000


class VideoViewSet(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = VideoPagination


class RecommendationsViewSet(generics.ListAPIView):
    queryset = Recommendations.objects.all().order_by('-pk')
    serializer_class = RecommendationsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GamesPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = _query_param = 'page_limit'
    max_page_size = 1000


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all().order_by('-pk')
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = GamesPagination


class ContactsViewSet(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AboutViewSet(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = (IsAdminOrReadOnly,)
