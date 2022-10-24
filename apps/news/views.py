from rest_framework import viewsets
from apps.base.permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
