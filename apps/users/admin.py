from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ExportActionModelAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from apps.users.models import User, Children
from apps.users.resources import UserResource, ChildrenResource


class ChildrenInline(admin.TabularInline):
    model = Children
    extra = 0


class UserAdmin(ExportActionModelAdmin):
    list_display = ['email']
    inlines = [ChildrenInline, ]
    resource_class = UserResource
    search_fields = ['email']
    exclude = ('code', 'password')


class ChildrenAdmin(ExportActionModelAdmin):
    list_display = ['id', 'name']
    resource_class = ChildrenResource


admin.site.register(User, UserAdmin)
admin.site.register(Children, ChildrenAdmin)

admin.site.unregister(Group)
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)
