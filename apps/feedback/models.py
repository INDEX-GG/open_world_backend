from django.db import models


class Feedback(models.Model):
    municipality = models.CharField(max_length=64, blank=True, null=True)
    family_status = models.CharField(max_length=64, blank=True, null=True)
    child_age = models.CharField(max_length=64, blank=True, null=True)
    disabled_person = models.CharField(max_length=64, blank=True, null=True)
    limited_person = models.CharField(max_length=64, blank=True, null=True)
    specialist = models.CharField(max_length=64, blank=True, null=True)
    counseling_theme = models.CharField(max_length=64, blank=True, null=True)
    other = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.municipality
