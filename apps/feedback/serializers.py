from rest_framework import serializers

from apps.feedback.models import Feedback, Questions, FeedbackMessage


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


class FeedbackMessageSerializer(serializers.ModelSerializer):
  class Meta:
      model = FeedbackMessage
      fields = ['name', 'email', 'phone', 'message']
