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
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = GamesPagination


def news_create():
    for i in range(1, 180):
        games = Games(title='Games' + str(i), description='Games' + str(i))
        games.save()
        images1 = GamesImages(games_id=i, src='images/games/1.jpg')
        images1.save()
        images2 = GamesImages(games_id=i, src='images/games/2.jpg')
        images2.save()
        images3 = GamesImages(games_id=i, src='images/games/3.jpg')
        images3.save()
