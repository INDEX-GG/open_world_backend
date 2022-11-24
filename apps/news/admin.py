from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.news.models import News, Images


class ImageInline(admin.TabularInline):
    model = Images
    extra = 0
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    preview.short_description = "Изображение"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [ImageInline, ]
