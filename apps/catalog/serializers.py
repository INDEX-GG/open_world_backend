from rest_framework import serializers
from apps.catalog.models import *


class ContentPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPdf
        fields = ['name', 'link', 'autoOpen']


class ContentImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImg
        fields = ['name', 'alt', 'url']


class TableAboutCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableAboutCenter
        fields = ('location', 'contacts', 'email', 'worktime',)


class TableContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableContacts
        fields = ['content_1', 'content_2', 'content_3']


class TableWorktimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableWorktime
        fields = ['content_1', 'content_2']


class TableDepartmentOMRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableDepartmentOMR
        fields = ['name', 'position', 'worktime', 'phone']


class TableDepartmentStSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableDepartmentSt
        fields = ['name', 'position', 'worktime', 'phone']


class TableDepartmentPPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableDepartmentPPP
        fields = ['name', 'position', 'worktime', 'phone']


class TableDepartmentCMRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableDepartmentCMR
        fields = ['name', 'position', 'worktime', 'phone']


class TableDepartmentDPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableDepartmentDP
        fields = ['name', 'position', 'worktime', 'phone']


class SectionAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionApp
        fields = ['description', 'image']


class SectionPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionPhone
        fields = ('phoneNumber', 'formatNumber', 'link')


class SectionPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionPartner
        fields = ('src', 'link')


class ContentSerializer(serializers.ModelSerializer):
    pdf = ContentPdfSerializer()
    img = ContentImgSerializer()
    table_vertical = serializers.SerializerMethodField()
    table_horizontal = serializers.SerializerMethodField()

    def get_table_vertical(self, obj):
        if obj.content_type:
            content_type = obj.content_type.model_class()
            queryset = content_type.objects.all()
        else:
            return None

        if obj.content_type.model == 'tablecontacts':
            serializer = TableContactsSerializer(queryset, many=True)
        elif obj.content_type.model == 'tableworktime':
            serializer = TableWorktimeSerializer(queryset, many=True)
        elif obj.content_type.model == 'tabledepartmentomr':
            serializer = TableDepartmentOMRSerializer(queryset, many=True)
        elif obj.content_type.model == 'tabledepartmentst':
            serializer = TableDepartmentStSerializer(queryset, many=True)
        elif obj.content_type.model == 'tabledepartmentppp':
            serializer = TableDepartmentPPPSerializer(queryset, many=True)
        elif obj.content_type.model == 'tabledepartmentcmr':
            serializer = TableDepartmentCMRSerializer(queryset, many=True)
        elif obj.content_type.model == 'tabledepartmentdp':
            serializer = TableDepartmentDPSerializer(queryset, many=True)
        else:
            serializer = None
        return serializer.data if serializer else None

    def get_table_horizontal(self, obj):
        if obj.table_horizontal:
            serializer = TableAboutCenterSerializer(obj.table_horizontal)
            return serializer.data
        return None

    class Meta:
        model = Content
        fields = ['type', 'text', 'pdf', 'img', 'table_vertical', 'table_horizontal']


class ElementsSerializer(serializers.ModelSerializer):
    # content = ContentSerializer(many=True)

    class Meta:
        model = Elements
        fields = ['slug', 'path', 'title']


class SearchPagesSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)

    class Meta:
        model = Elements
        fields = ['slug', 'path', 'title', 'content']


class SectionsDataSerializer(serializers.ModelSerializer):
    app = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    partners = serializers.SerializerMethodField()
    elements = serializers.SerializerMethodField()

    class Meta:
        model = Sections
        fields = ['app', 'phone', 'partners', 'elements']

    def get_app(self, obj):
        app = obj.section_app.first()  # Retrieve the first related SectionApp object
        if app:
            return SectionAppSerializer(app).data
        return None

    def get_phone(self, obj):
        phone = obj.section_phone.first()
        if phone:
            return SectionPhoneSerializer(phone).data
        return None

    def get_partners(self, obj):
        partners = obj.section_partner.all()
        if partners:
            return SectionPartnerSerializer(partners, many=True).data
        return None

    def get_elements(self, obj):
        elements = obj.section.all()  # Use reverse relationship
        if elements:
            return ElementsSerializer(elements, many=True).data
        return None


class SectionsJSONSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.CharField()
    path = serializers.CharField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = Sections
        fields = ['title', 'slug', 'path', 'data']

    def get_data(self, obj):
        sections_data = Sections.objects.filter(id=obj.id).first()  # Retrieve the current Sections object
        if sections_data:
            return SectionsDataSerializer(sections_data).data  # Serialize the single object directly
        return None