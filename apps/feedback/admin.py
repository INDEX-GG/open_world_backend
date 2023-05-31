from django.contrib import admin
from apps.feedback.models import Questions, FeedbackMessage

admin.site.register(Questions)
admin.site.register(FeedbackMessage)
