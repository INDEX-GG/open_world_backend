from django.db import models


class Video(models.Model):
    url = models.CharField('Ссылка на видео', max_length=255)
    description = models.TextField('Описание видео')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['pk']


class Games(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'


class GamesImages(models.Model):
    images = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка', upload_to='images/games/')

    class Meta:
        verbose_name = 'Картинки для игр'
        verbose_name_plural = 'Картинки для игр'

    def src(self):
        url = self.image.url
        return url
