from django.contrib import admin
from apps.feedback.models import Questions, Feedback

admin.site.register(Feedback)
admin.site.register(Questions)

