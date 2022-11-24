from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from apps.news.serializers import NewsSerializer
from apps.news.models import News


class NewsViewSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_limit'
    max_page_size = 1000


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-pk')
    serializer_class = NewsSerializer
    pagination_class = NewsViewSetPagination


class NewsItemAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
