from django.contrib import admin
from apps.catalog.models import Sections, Elements, Content, ContentPdf, ContentImg, TableContacts, TableAboutCenter, \
    TableWorktime, TableDepartmentOMR, TableDepartmentSt, TableDepartmentPPP, TableDepartmentCMR, TableDepartmentDP, \
    SectionApp, SectionPhone, SectionPartner


admin.site.site_header = 'Панель администратора'


class ContentImgInline(admin.TabularInline):
    model = ContentImg
    extra = 0


class ContentInline(admin.TabularInline):
    model = Content
    extra = 0
    fields = ['type', 'text', 'pdf', 'img']
    inlines = [ContentImgInline, ]


class SectionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'path']
    readonly_fields = ('slug', 'path')
    ordering = ['id']


# access only for superuser
class SectionAppAdmin(admin.ModelAdmin):
    list_display = ['section', 'description', 'image']
    ordering = ['id']


# access only for superuser
class SectionPhoneAdmin(admin.ModelAdmin):
    list_display = ['section', 'phoneNumber', 'formatNumber', 'link']
    ordering = ['id']


# access only for superuser
class SectionPartnerAdmin(admin.ModelAdmin):
    list_display = ['section', 'src', 'link', 'file']
    ordering = ['id']


class ElementsAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_section_title', 'slug', 'path', ]
    fields = ('title', 'section', 'slug', 'path')
    readonly_fields = ('slug', 'path')
    ordering = ['id']
    inlines = [ContentInline, ]
    list_filter = ('section',)

    def get_section_title(self, obj):
        return obj.section.title if obj.section else None

    get_section_title.short_description = 'Раздел сайта'



class ContentAdmin(admin.ModelAdmin):
    list_display = ['element', 'type']
    fields = ('element', 'type', 'text', 'pdf', 'img', 'content_type', 'table_horizontal')
    ordering = ['id']
    list_filter = ('element',)


class ContentPdfAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'autoOpen']
    fields = ['name', 'autoOpen', 'file']

    ordering = ['id']


class ContentImgAdmin(admin.ModelAdmin):
    list_display = ['name', 'alt', 'url']
    fields = ['name', 'alt', 'file']
    ordering = ['id']


class TableContactsAdmin(admin.ModelAdmin):
    list_display = ['content_1', 'content_2', 'content_3']
    ordering = ['id']


class TableAboutCenterAdmin(admin.ModelAdmin):
    list_display = ['location', 'contacts', 'email', "worktime"]
    ordering = ['id']


class TableWorktimeAdmin(admin.ModelAdmin):
    list_display = ['content_1', 'content_2']
    ordering = ['id']


class TableDepartmentOMRAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'worktime', 'phone']
    ordering = ['id']


class TableDepartmentStAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'worktime', 'phone']
    ordering = ['id']


class TableDepartmentPPPAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'worktime', 'phone']
    ordering = ['id']


class TableDepartmentCMRAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'worktime', 'phone']
    ordering = ['id']


class TableDepartmentDPAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'worktime', 'phone']
    ordering = ['id']


admin.site.register(Sections, SectionsAdmin)
admin.site.register(SectionApp, SectionAppAdmin)
admin.site.register(SectionPhone, SectionPhoneAdmin)
admin.site.register(SectionPartner, SectionPartnerAdmin)
admin.site.register(Elements, ElementsAdmin)
admin.site.register(ContentPdf, ContentPdfAdmin)
admin.site.register(ContentImg, ContentImgAdmin)
admin.site.register(TableContacts, TableContactsAdmin)
admin.site.register(TableAboutCenter, TableAboutCenterAdmin)
admin.site.register(TableWorktime, TableWorktimeAdmin)
admin.site.register(TableDepartmentOMR, TableDepartmentOMRAdmin)
admin.site.register(TableDepartmentSt, TableDepartmentStAdmin)
admin.site.register(TableDepartmentPPP, TableDepartmentPPPAdmin)
admin.site.register(TableDepartmentCMR, TableDepartmentCMRAdmin)
admin.site.register(TableDepartmentDP, TableDepartmentDPAdmin)
