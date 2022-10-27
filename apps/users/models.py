from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField('email address', unique=True, max_length=255)
    is_verified = models.BooleanField(default=False)
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
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

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


# TODO: Проверка email на уникальность, создание новой записи при новом коде
# TODO: Удаление модели при успешной регистрации пользователя
class EmailCode(models.Model):
    email = models.CharField('email', max_length=64, unique=True)
    code = models.CharField('code', max_length=6)

    def __str__(self):
        return self.email
