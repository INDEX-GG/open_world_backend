from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    name = models.CharField('Имя', blank=True, max_length=100)
    lastname = models.CharField('Фамилия', blank=True, max_length=100)
    patronymic = models.CharField('Отчество', blank=True, max_length=100)
    phone = models.CharField('Номер телефона', blank=True, max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Children(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField('Имя', blank=True, max_length=100)
    lastname = models.CharField('Фамилия', blank=True, max_length=100)
    patronymic = models.CharField('Отчество', blank=True, max_length=100)
    age = models.CharField('Возраст', blank=True, max_length=100)
    disability = models.BooleanField('Инвалидность', default=False)
    program_number = models.CharField('Номер программы', blank=True, max_length=100)

    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.program_number

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
