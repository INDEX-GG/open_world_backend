# Generated by Django 4.1.2 on 2022-10-25 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='src',
        ),
    ]
