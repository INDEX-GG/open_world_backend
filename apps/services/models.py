from django.db import models


class ServicesForm(models.Model):
    services_name = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    communication = models.CharField(max_length=255, blank=True, null=True)


class Services(models.Model):
    title = models.JSONField("Файл", blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = 'Сервисы'
        verbose_name_plural = 'Сервисы'
        ordering = ['pk']
