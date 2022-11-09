from django.db import models


class Feedback(models.Model):
    municipality = models.CharField(max_length=255, blank=True, null=True)
    family_status = models.CharField(max_length=255, blank=True, null=True)
    child_age = models.CharField(max_length=255, blank=True, null=True)
    disabled_person = models.CharField(max_length=255, blank=True, null=True)
    limited_person = models.CharField(max_length=255, blank=True, null=True)
    specialist = models.CharField(max_length=255, blank=True, null=True)
    counseling_theme = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    communication = models.CharField(max_length=255, blank=True, null=True)


class Questions(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'
        ordering = ['-pk']
