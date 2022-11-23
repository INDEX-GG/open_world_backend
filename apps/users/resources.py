from import_export import resources
from import_export.fields import Field

from .models import User, Children


class UserResource(resources.ModelResource):
    email = Field(attribute='email', column_name='Email')
    name = Field(attribute='name', column_name='Имя')
    lastname = Field(attribute='lastname', column_name='Фамилия')
    patronymic = Field(attribute='patronymic', column_name='Отчество')
    phone = Field(attribute='phone', column_name='Телефон')
    count_children = Field(attribute='count_children', column_name='Кол-во детей')

    class Meta:
        model = User
        fields = ('email', 'name', 'lastname', 'patronymic', 'phone', 'count_children')


class ChildrenResource(resources.ModelResource):
    user = Field(attribute='user', column_name='Родитель')
    name = Field(attribute='name', column_name='Имя')
    lastname = Field(attribute='lastname', column_name='Фамилия')
    patronymic = Field(attribute='patronymic', column_name='Отчество')
    age = Field(attribute='age', column_name='Возраст')
    disability_convert = Field(attribute='disability_convert', column_name='Инвалидность')
    program_number = Field(attribute='program_number', column_name='Номер программы')

    class Meta:
        model = Children
        fields = ('user', 'name', 'lastname', 'patronymic', 'age', 'disability_convert', 'program_number')
