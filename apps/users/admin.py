from django.contrib import admin
from .models import User, Children, EmailCode

admin.site.register(User)
admin.site.register(Children)
admin.site.register(EmailCode)
