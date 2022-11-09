from django.contrib import admin
from .models import (
    Video, GamesImages, Games, Contacts, About, AboutDocs, RecommendationsDocs, Recommendations)

admin.site.register(Video)
admin.site.register(Contacts)


class GamesImageInline(admin.TabularInline):
    model = GamesImages
    extra = 0


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [GamesImageInline, ]


class RecommendationsDocsInline(admin.TabularInline):
    model = RecommendationsDocs
    extra = 0


@admin.register(Recommendations)
class RecommendationsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [RecommendationsDocsInline, ]


class AboutDocsInline(admin.TabularInline):
    model = AboutDocs
    extra = 0


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [AboutDocsInline, ]
