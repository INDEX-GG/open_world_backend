from django.db import models


class AppLink(models.Model):
    file = models.FileField('Сборка приложения', upload_to='build/file/')
    date = models.DateField('Дата загрузки')

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложение'
        ordering = ['-pk']
