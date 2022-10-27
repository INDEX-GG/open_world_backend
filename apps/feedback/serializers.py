# from rest_framework import serializers
#
#
# class FeedbackSerializer(serializers.Serializer):
#     municipality = serializers.CharField(max_length=64)
#     family_status = serializers.CharField(max_length=64)
#     child_age = serializers.CharField(max_length=64)
#     disabled_person = serializers.CharField(max_length=64)
#     limited_person = serializers.CharField(max_length=64)
#     specialist = serializers.CharField(max_length=64)
#     counseling_theme = serializers.CharField(max_length=64)
#     other = serializers.CharField(max_length=64)
#     phone = serializers.CharField(max_length=64)
#     email = serializers.CharField(max_length=64)
#  def create(self, validated_data):
#         return Feedback(**validated_data)