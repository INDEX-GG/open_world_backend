# Generated by Django 4.1.2 on 2022-11-09 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_docs_doc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Docs',
        ),
    ]