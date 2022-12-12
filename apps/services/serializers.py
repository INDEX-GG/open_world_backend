from rest_framework import serializers

from apps.services.models import (
    ServicesForm, Services)


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


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'
