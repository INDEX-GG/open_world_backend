from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('The Email must be set')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


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

    name = models.CharField('Имя', blank=True, max_length=100)
    lastname = models.CharField('Фамилия', blank=True, max_length=100)
    patronymic = models.CharField('Отчество', blank=True, max_length=100)
    phone = models.CharField('Номер телефона', blank=True, max_length=100)

    def __str__(self):
        return self.email

    def tokens(self):
        return ''

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
        return self.name + ' ' + self.lastname + ' ' + self.program_number

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'


class EmailCode(models.Model):
    email = models.CharField('email', max_length=100)
    code = models.CharField('code', max_length=100)

    def __str__(self):
        return self.email
