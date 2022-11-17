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


class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = VideoPagination


class GamesPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = _query_param = 'page_limit'
    max_page_size = 1000


class GamesAPIView(generics.ListAPIView):
    queryset = Games.objects.all().order_by('-pk')
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = GamesPagination


class GamesItemAPIView(generics.RetrieveAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RecommendationsAPIView(generics.ListAPIView):
    queryset = Recommendations.objects.all().order_by('-pk')
    serializer_class = RecommendationsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ContactsAPIView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = (IsAdminOrReadOnly,)
