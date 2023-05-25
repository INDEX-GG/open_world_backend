from rest_framework import generics
from rest_framework.views import APIView
from apps.catalog.serializers import *
from apps.catalog.models import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.news.models import News
from apps.news.serializers import NewsSerializer


class ContentAPIView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ElementAPIView(generics.ListAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer


class SectionsAPIView(generics.ListAPIView):
    queryset = Sections.objects.all()
    serializer_class = SectionsJSONSerializer


class TableContactsAPIView(generics.ListAPIView):
    queryset = TableContacts.objects.all()
    serializer_class = TableContactsSerializer


class TableWorktimeAPIView(generics.ListAPIView):
    queryset = TableWorktime.objects.all()
    serializer_class = TableWorktimeSerializer


class ContentElementsAPIView(APIView):
    def get(self, request, path_value):
        try:
            elements = Elements.objects.get(path=path_value)  # Найти Elements по динамическому значению пути
            content = elements.content.all()  # Получить связанные с Elements объекты Content

            serializer = ContentSerializer(content, many=True)  # Инициализировать сериализатор для сериализации Content

            return Response(serializer.data, status=status.HTTP_200_OK)  # Вернуть сериализованные данные Content
        except Elements.DoesNotExist:
            return Response("Страница не найдена", status=status.HTTP_404_NOT_FOUND)


class SearchAPIView(APIView):
    def post(self, request):
        search_query = request.data.get('find', None)

        if search_query is not None:

            results = Elements.objects.filter(
                Q(title__icontains=search_query) |
                Q(content__text__icontains=search_query) |
                Q(content__pdf__name__icontains=search_query) |
                Q(content__img__name__icontains=search_query)
            )
            serializer = SearchPagesSerializer(results, many=True)

            # Дополнительный поиск в модели News
            news_results = News.objects.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
            news_serializer = NewsSerializer(news_results, many=True)
            serialized_news = news_serializer.data

            # Формирование результата поиска
            response_data = []

            # Добавление результатов поиска из модели Elements
            response_data.append({
                "page": serializer.data
            })

            # Добавление результатов поиска из модели News
            response_data.append({
                "news": serialized_news
            })

            return Response(response_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
