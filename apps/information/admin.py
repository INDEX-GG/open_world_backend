from django.contrib import admin
from .models import Video, GamesImages, Games

admin.site.register(Video)


class GamesImageInline(admin.TabularInline):
    model = GamesImages
    extra = 0


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [GamesImageInline, ]

