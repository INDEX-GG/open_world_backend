from rest_framework import serializers
from .models import EmailCode


class EmailCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCode
        fields = '__all__'
