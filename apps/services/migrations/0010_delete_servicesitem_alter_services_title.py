# Generated by Django 4.1.3 on 2022-12-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_services_title_alter_servicesitem_services'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServicesItem',
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.JSONField(blank=True, max_length=255, null=True, verbose_name='Файл'),
        ),
    ]
