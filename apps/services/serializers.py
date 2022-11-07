from rest_framework import serializers

from .models import ServicesOffline


class ServicesOfflineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesOffline
        fields = ['name', 'lastname', 'patronymic',
                  'email', 'phone', 'communication', 'question', 'services_name']


class ServicesVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesOffline
        fields = ['name', 'lastname', 'patronymic',
                  'email', 'question', 'services_name']
