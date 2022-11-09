from rest_framework import serializers

from .models import Feedback, Questions


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['municipality', 'family_status', 'child_age',
                  'disabled_person', 'limited_person', 'specialist',
                  'counseling_theme', 'other', 'phone', 'email', 'communication']


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'title', 'description']
