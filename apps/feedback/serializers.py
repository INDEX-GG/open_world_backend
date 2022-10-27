from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['municipality', 'family_status', 'child_age',
                  'disabled_person', 'limited_person', 'specialist',
                  'counseling_theme', 'other', 'phone', 'email']
