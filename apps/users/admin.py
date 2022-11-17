from django.contrib import admin
from .models import User, Children


class ChildrenInline(admin.TabularInline):
    model = Children
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['email']
    inlines = [ChildrenInline, ]
