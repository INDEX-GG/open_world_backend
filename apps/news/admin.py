from django.contrib import admin
from .models import News, Images


class ImageInline(admin.TabularInline):
    model = Images
    extra = 0


@admin.register(News)
class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [ImageInline, ]

