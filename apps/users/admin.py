from django.contrib import admin
from django.contrib.auth.models import Group

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from .models import User, Children


class ChildrenInline(admin.TabularInline):
    model = Children
    extra = 0


class UserResource(resources.ModelResource):
    name = Field(attribute='name', column_name='Имя')

    class Meta:
        model = User
        fields = ('email', 'name', 'lastname', 'patronymic', 'phone')


class User1Admin(ImportExportModelAdmin):
    save_on_top = True
    list_display = ['email']
    inlines = [ChildrenInline, ]
    resource_class = UserResource
    search_fields = ['email']
    exclude = ('code', 'password')


admin.site.register(User, User1Admin)
admin.site.unregister(Group)
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)
