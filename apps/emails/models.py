from django.db import models


class EmailCode(models.Model):
    email = models.CharField('email', max_length=100)
    code = models.CharField('code', max_length=100)

    def __str__(self):
        return self.email
