# Generated by Django 4.1.2 on 2022-10-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_emailcode_code_alter_emailcode_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=100, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='emailcode',
            name='code',
            field=models.CharField(max_length=6, verbose_name='code'),
        ),
    ]
