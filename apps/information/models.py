from django.db import models


class Video(models.Model):
    url = models.CharField('Ссылка на видео', max_length=255)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['-pk']


class Games(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'


class GamesImages(models.Model):
    games = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='games')
    src = models.ImageField('image', upload_to='images/games/')

    class Meta:
        verbose_name = 'Картинки для игр'
        verbose_name_plural = 'Картинки для игр'
