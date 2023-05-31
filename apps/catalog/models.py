from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from slugify import slugify as unicode_slugify
from datetime import datetime
import os


def validate_image_extension(value):
    ext = value.name.split('.')[-1].lower()
    if ext not in ['jpeg', 'jpg', 'webp', 'png']:
        raise ValidationError('Неправильный формат изображения. Разрешены только JPEG, JPG, WEBP и PNG форматы.')


class TableAboutCenter(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name='Место нахождения учреждения')
    content_2 = models.CharField(max_length=255, verbose_name='Телефоны/факс')
    content_3 = models.CharField(max_length=255, verbose_name='E-mail')
    content_4 = models.CharField(max_length=255, verbose_name='Режим работы')

    def __str__(self):
        return "Таблица - О центре"

    class Meta:
        ordering = ['id']
        verbose_name = '2 - Таблица - О центре'
        verbose_name_plural = '2 - Таблица - О центре'


class TableContacts(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name='Наименование')
    content_2 = models.CharField(max_length=255, verbose_name='Адрес')
    content_3 = models.CharField(max_length=255, verbose_name='Телефон')

    class Meta:
        ordering = ['id']
        verbose_name = '3 - Таблица - Контакты'
        verbose_name_plural = '3 - Таблица - Контакты'


class TableWorktime(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name='Дни недели')
    content_2 = models.CharField(max_length=255, verbose_name='Время работы')

    class Meta:
        ordering = ['id']
        verbose_name = '4 - Таблица - Режим работы'
        verbose_name_plural = '4 - Таблица - Режим работы'


### 1 Таблица - Отделение организационно-методической работы
class TableDepartmentOMR(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name="ФИО")
    content_2 = models.CharField(max_length=255, verbose_name="Должность")
    content_3 = models.CharField(max_length=255, verbose_name="Режим Работы")
    content_4 = models.CharField(max_length=255, verbose_name="Телефон")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица - Отделение организационно-методической работы'
        verbose_name_plural = 'Таблица - Отделение организационно-методической работы'


### 2 Таблица - Стационарное отделение
class TableDepartmentSt(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name="ФИО")
    content_2 = models.CharField(max_length=255, verbose_name="Должность")
    content_3 = models.CharField(max_length=255, verbose_name="Режим Работы")
    content_4 = models.CharField(max_length=255, verbose_name="Телефон")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица - Стационарное отделение'
        verbose_name_plural = 'Таблица - Стационарное отделение'


### 3 Таблица - Отделение психолого-педагогической помощи
class TableDepartmentPPP(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name="ФИО")
    content_2 = models.CharField(max_length=255, verbose_name="Должность")
    content_3 = models.CharField(max_length=255, verbose_name="Режим Работы")
    content_4 = models.CharField(max_length=255, verbose_name="Телефон")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица - Отделение психолого-педагогической помощи'
        verbose_name_plural = 'Таблица - Отделение психолого-педагогической помощи'


### 4 Таблица - Отделение социально-медицинской реабилитации
class TableDepartmentCMR(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name="ФИО")
    content_2 = models.CharField(max_length=255, verbose_name="Должность")
    content_3 = models.CharField(max_length=255, verbose_name="Режим Работы")
    content_4 = models.CharField(max_length=255, verbose_name="Телефон")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица - Отделение социально-медицинской реабилитации'
        verbose_name_plural = 'Таблица - Отделение социально-медицинской реабилитации'


### 5 Таблица - Отделение дневного пребывания
class TableDepartmentDP(models.Model):
    content_1 = models.CharField(max_length=255, verbose_name="ФИО")
    content_2 = models.CharField(max_length=255, verbose_name="Должность")
    content_3 = models.CharField(max_length=255, verbose_name="Режим Работы")
    content_4 = models.CharField(max_length=255, verbose_name="Телефон")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица - Отделение дневного пребывания'
        verbose_name_plural = 'Таблица - Отделение дневного пребывания'


class Sections(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок раздела')
    slug = models.CharField(max_length=255, verbose_name='slug-поле', unique=True)   ### "glavnaya",
    path = models.CharField(max_length=255, verbose_name='Путь к странице', unique=True)   ### "/glavnaya",

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "0 - Раздел"
        verbose_name_plural = "0 - Разделы"


class SectionApp(models.Model):
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='section_app', verbose_name='Раздел',
                                null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name="Текст/Описание")
    image = models.CharField(max_length=255, verbose_name="Путь к картинке")

    class Meta:
        ordering = ['id']
        verbose_name = "1.4 - Приложение Открытый мир"
        verbose_name_plural = "1.4 - Приложение Открытый мир"


class SectionPhone(models.Model):
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='section_phone', verbose_name='Раздел',
                                null=True, blank=True)
    phoneNumber = models.PositiveBigIntegerField(verbose_name="Номер телефона")
    formatNumber  = models.CharField(max_length=50, verbose_name="Номер телефона форматированный")
    link = models.CharField(max_length=255, verbose_name="Ссылка")

    class Meta:
        ordering = ['id']
        verbose_name = "1.5 - Единый контактный центр"
        verbose_name_plural = "1.5 - Единый контактный центр"


class SectionPartner(models.Model):
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='section_partner', verbose_name='Раздел',
                                null=True, blank=True)
    src = models.CharField(max_length=255, verbose_name="Путь к картинке")
    link = models.CharField(max_length=255, verbose_name="Ссылка на ресурс", blank=True)
    file = models.ImageField(blank=True, verbose_name='Изображения', upload_to='images/', null=True)

    class Meta:
        ordering = ['id']
        verbose_name = "1.6 - Партнера"
        verbose_name_plural = "1.6 - Партнеры"


class ContentImg(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя картинки', unique=True)
    alt = models.CharField(max_length=255, verbose_name='Альт текст', blank=True, default='')
    url = models.CharField(max_length=255, verbose_name='Ссылка', blank=True, default='')
    file = models.ImageField(blank=True, verbose_name='Изображение', upload_to='images/', null=True, validators=[validate_image_extension])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "1.2 - Изображение"
        verbose_name_plural = "1.2 - Изображения"

    def save(self, *args, **kwargs):
        timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
        file_extension = os.path.splitext(self.file.name)[1]
        divider = '_'
        self.file.name = f'{unicode_slugify(self.name)}{divider}{timestamp}{file_extension}'
        self.url = '/media/images/' + self.file.name
        super().save(*args, **kwargs)


class ContentPdf(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя файла', unique=True)
    link = models.CharField(max_length=255, verbose_name='Ссылка', null=True, blank=True)
    autoOpen = models.BooleanField(default=True, verbose_name='Развернут')
    file = models.FileField(blank=True, verbose_name='PDF-файл', upload_to='pdf/', null=True, validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "1.3 - PDF-файл"
        verbose_name_plural = "1.3 - PDF-файлы"

    def save(self, *args, **kwargs):
        timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
        file_extension = os.path.splitext(self.file.name)[1]
        divider = '_'
        self.file.name = f'{unicode_slugify(self.name)}{divider}{timestamp}{file_extension}'
        self.link = '/media/pdf/' + self.file.name
        super().save(*args, **kwargs)


class Elements(models.Model):
    slug = models.CharField(max_length=255, verbose_name='SLUG', unique=True, blank=True)
    path = models.CharField(max_length=255, verbose_name='Путь к странице', unique=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название страницы', unique=True)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='section',  verbose_name='Раздел', null=True, blank=True)

    def save(self, *args, **kwargs):
        if (self.title != 'Новости') and (self.title != 'Государственное задание'):
            # Генерация значения slug на основе транслитерации поля title
            self.slug = unicode_slugify(self.title)
            # Генерация значения path на основе Sections.path и Elements.slug
            self.path = f"{self.section.path}/{self.slug}"
        super().save(*args, **kwargs)

    def validate_unique(self, exclude=None):
        if self.title.lower() in ['главная', 'контакты', 'карта сайта', 'обратная связь']:
            raise ValidationError(f"Страница с таким названием уже есть, введите другое значение")

    def clean(self):
        self.validate_unique()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "1 - Страницу"
        verbose_name_plural = "1 - Страницы"


class Content(models.Model):
    TYPE_CHOICES = (
        ('text', 'Текст'),
        ('img', 'Изображение'),
        ('pdf', 'PDF-файл'),
        ('map', 'Карта - как пройти'),
        ('table_horizontal', 'Горизонтальная таблица'),
        ('table_vertical', 'Вертикальная таблица'),
    )
    element = models.ForeignKey(Elements, on_delete=models.CASCADE, related_name='content',  verbose_name='Страница')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип контента")
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    pdf = models.OneToOneField(
        ContentPdf, on_delete=models.CASCADE, null=True, blank=True, verbose_name='PDF-файл'
    )
    img = models.OneToOneField(
        ContentImg, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Картинка'
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        limit_choices_to={
            "model__in": [
                'tablecontacts',
                'tableworktime',
                'tabledepartmentomr',
                'tabledepartmentst',
                'tabledepartmentppp',
                'tabledepartmentcmr',
                'tabledepartmentdp',
            ]
        },
        null=True, blank=True,
        verbose_name='Вертикальная таблица'
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    table_vertical = GenericForeignKey('content_type', 'object_id')
    table_horizontal = models.OneToOneField(
        TableAboutCenter, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.element.title

    class Meta:
        ordering = ['id']
        verbose_name = "1.1 - Контент страницы"
        verbose_name_plural = "1.1 - Контент страниц"


class GosTask(models.Model):
    pdf = models.OneToOneField(
        ContentPdf, on_delete=models.CASCADE, null=True, blank=True, verbose_name='PDF-файл'
    )

    def __str__(self):
        return 'Государственное задание'

    class Meta:
        ordering = ['-id']
        verbose_name = "1.1 - Государственное задание"
        verbose_name_plural = "1.1 - Государственное задание"
