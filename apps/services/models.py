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
    title = models.CharField('Должность', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервисы'
        verbose_name_plural = 'Сервисы'
        ordering = ['pk']


class ServicesItem(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services')
    job = models.CharField('Должность', blank=True, null=True, max_length=255)
    address = models.CharField('Адрес', blank=True, null=True, max_length=255)
    phone = models.CharField('Телефон', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.job

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
        ordering = ['pk']
