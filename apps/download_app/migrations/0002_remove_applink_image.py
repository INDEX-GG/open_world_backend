# Generated by Django 4.1.3 on 2022-12-15 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applink',
            name='image',
        ),
    ]
