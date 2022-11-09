from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from apps.base.permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer
from .models import News


class NewsViewSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_limit'
    max_page_size = 1000


class NewsViewSet(generics.ListAPIView):
    queryset = News.objects.all().order_by('-pk')
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = NewsViewSetPagination


class NewsItemViewSet(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
