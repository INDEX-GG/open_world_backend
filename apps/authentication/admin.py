from django.contrib import admin
from .models import EmailCode, ResetEmailCode

admin.site.register(EmailCode)
admin.site.register(ResetEmailCode)
