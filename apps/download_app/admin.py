from django.contrib import admin

from apps.download_app.models import AppLink


@admin.register(AppLink)
class AppLinkAdmin(admin.ModelAdmin):
    list_display = ['date']
