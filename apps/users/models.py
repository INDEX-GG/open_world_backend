import json

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken

from ..authentication.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField('email address', unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    code = models.CharField('Код', blank=True, max_length=100)
    name = models.CharField('Имя', blank=True, max_length=100)
    lastname = models.CharField('Фамилия', blank=True, max_length=100)
    patronymic = models.CharField('Отчество', blank=True, max_length=100)
    phone = models.CharField('Номер телефона', blank=True, max_length=100)

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return json.dumps({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Children(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parents_children')
    name = models.CharField('Имя', blank=True, max_length=100)
    lastname = models.CharField('Фамилия', blank=True, max_length=100)
    patronymic = models.CharField('Отчество', blank=True, max_length=100)
    age = models.CharField('Возраст', blank=True, max_length=100)
    disability = models.BooleanField('Инвалидность', default=False)
    program_number = models.CharField('Номер программы', blank=True, max_length=100)

    def __str__(self):
        return self.name + ' ' + self.lastname

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
