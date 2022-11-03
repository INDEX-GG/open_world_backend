from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from apps.base.permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer
from .models import News, Images


class NewsViewSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_limit'
    max_page_size = 1000


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-pk')
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = NewsViewSetPagination


def news_create():
    for i in range(204, 404):
        new = News(title='News' + str(i), description='News' + str(i))
        new.save()
        images1 = Images(news_id=i, src='images/news/1.jpg')
        images1.save()
        images2 = Images(news_id=i, src='images/news/2.jpg')
        images2.save()
        images3 = Images(news_id=i, src='images/news/3.jpg')
        images3.save()
