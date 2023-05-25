from rest_framework import serializers

from apps.news.models import News, Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'news', 'src']


class NewsSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'created_at', 'images']
