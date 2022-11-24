from rest_framework import serializers

from apps.information.models import (
    Video, Games, GamesImages, Contacts, About, AboutDocs, Recommendations, RecommendationsDocs)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class RecommendationsDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationsDocs
        fields = ['id', 'title', 'src']


class RecommendationsSerializer(serializers.ModelSerializer):
    recommendations = RecommendationsDocsSerializer(many=True, read_only=True)

    class Meta:
        model = Recommendations
        fields = ['id', 'title', 'recommendations']


class GamesImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesImages
        fields = ['id', 'src']


class GamesSerializer(serializers.ModelSerializer):
    images = GamesImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Games
        fields = ['id', 'title', 'description', 'images']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class AboutDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutDocs
        fields = ['id', 'title', 'src']


class AboutSerializer(serializers.ModelSerializer):
    about = AboutDocsSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['id', 'title', 'about']
