from django.db import models

from .utils import Util


class Video(models.Model):
    url = models.CharField('Ссылка на видео', max_length=255)
    description = models.TextField('Описание видео', blank=True, null=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.description == '':
            self.description = Util.get_description(str(self.url))
        super(Video, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Видеоуроки'
        verbose_name_plural = 'Видеоуроки'
        ordering = ['pk']


class Games(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игры для развития'
        verbose_name_plural = 'Игры для развития'


class GamesImages(models.Model):
    images = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка', upload_to='images/games/')

    class Meta:
        verbose_name = 'Картинки для игр'
        verbose_name_plural = 'Картинки для игр'

    def src(self):
        url = self.image.url
        return url


class Contacts(models.Model):
    title = models.CharField('Заголовок', blank=True, null=True, max_length=255)
    address = models.CharField('Адрес', blank=True, null=True, max_length=255)
    phone = models.CharField('Телефон', blank=True, null=True, max_length=255)
    site = models.CharField('Сайт', blank=True, null=True, max_length=255)
    vk = models.CharField('VK', blank=True, null=True, max_length=255)
    telegram = models.CharField('Telegram', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class About(models.Model):
    title = models.TextField('Заголовок', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О центре'
        verbose_name_plural = 'О центре'


class AboutDocs(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about')
    title = models.CharField('Заголовок', blank=True, null=True, max_length=255)
    docs = models.FileField(blank=True, null=True, upload_to='docs/about/')

    def __str__(self):
        return self.title

    def src(self):
        url = self.docs.url
        return url

    class Meta:
        verbose_name = 'Документация в разделе о нас'
        verbose_name_plural = 'Документация в разделе о нас'


class Recommendations(models.Model):
    title = models.TextField('Ссылка на youtube канал', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рекомендации'
        verbose_name_plural = 'Рекомендации'


class RecommendationsDocs(models.Model):
    recommendations = models.ForeignKey(Recommendations, on_delete=models.CASCADE, related_name='recommendations')
    title = models.CharField('Заголовок', blank=True, null=True, max_length=255)
    docs = models.FileField(blank=True, null=True, upload_to='docs/recommendations/')

    def __str__(self):
        return self.title

    def src(self):
        url = self.docs.url
        return url

    class Meta:
        verbose_name = 'Методические материалы'
        verbose_name_plural = 'Методические материалы'
