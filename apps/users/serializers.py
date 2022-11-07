from rest_framework import serializers

from .models import User, Children


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ['id', 'user', 'name', 'lastname', 'patronymic', 'age', 'disability', 'program_number']


class ChildrenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ['id', 'name', 'lastname', 'patronymic', 'age', 'disability', 'program_number']


class UserSerializer(serializers.ModelSerializer):
    parents_children = ChildrenSerializer(many=True, read_only=True)
    email = serializers.EmailField(max_length=64, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'lastname', 'patronymic', 'phone', 'parents_children']
