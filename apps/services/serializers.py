from rest_framework import serializers

from apps.services.models import (
    ServicesForm, Services, ServicesItem)


class ServicesOfflineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesForm
        fields = ['name', 'lastname', 'patronymic',
                  'email', 'phone', 'communication', 'question', 'services_name']


class ServicesVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesForm
        fields = ['name', 'lastname', 'patronymic',
                  'email', 'question', 'services_name']


class ServicesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesItem
        fields = ['id', 'job', 'address', 'phone']


class ServicesSerializer(serializers.ModelSerializer):
    services = ServicesItemSerializer(many=True, read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'title', 'services']
