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
    queryset = Games.objects.all().order_by('-pk')
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = GamesPagination


def news_create():
    for i in range(181, 281):
        games = Games(title='Games' + str(i),
                      description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed maximus quam turpis, ut porttitor est viverra sed. Cras iaculis malesuada mollis. Nam non aliquam lacus, auctor volutpat turpis. Maecenas interdum, erat sit amet scelerisque iaculis, augue sem elementum nunc, ut volutpat risus nisl a odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam eget imperdiet erat. Proin suscipit nisi vitae finibus mattis. Morbi ultricies velit erat, ac malesuada nibh laoreet sed. Aliquam erat volutpat. Suspendisse auctor imperdiet consequat.Vivamus ac tristique orci. Proin consequat elit a elit dapibus, in molestie nulla porta. Etiam pellentesque, dolor eget commodo semper, neque ante tincidunt felis, pharetra imperdiet tortor purus a velit. Cras at metus elit. Nam justo odio, accumsan a mi vel, vulputate dictum tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tincidunt condimentum ex imperdiet pulvinar. Donec finibus vehicula lorem eu varius. Integer suscipit facilisis nulla, quis sagittis nisi lobortis a. Phasellus pulvinar laoreet neque fermentum varius. Donec consectetur, purus vel hendrerit malesuada, nibh nisl efficitur nibh, id pretium diam arcu vel est. Duis non velit varius, molestie ex ut, ultricies nibh. Pellentesque in lorem fringilla, pharetra lacus tristique, condimentum orci. Nulla id hendrerit.' + str(
                          i))
        games.save()
        images1 = GamesImages(images_id=i, src='images/games/1.jpg')
        images1.save()
        images2 = GamesImages(images_id=i, src='images/games/2.jpg')
        images2.save()
        images3 = GamesImages(images_id=i, src='images/games/3.jpg')
        images3.save()
