from django.contrib import admin
from .models import Services, ServicesItem


class ServicesItemInline(admin.TabularInline):
    model = ServicesItem
    extra = 0


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title']
    inlines = [ServicesItemInline, ]


