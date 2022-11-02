from rest_framework import serializers
from .models import Video, Games, GamesImages


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class GamesImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesImages
        fields = ['id', 'images', 'src']


class GamesSerializer(serializers.ModelSerializer):
    images = GamesImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Games
        fields = ['id', 'title', 'description', 'images']
