# Generated by Django 4.1.3 on 2023-05-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tableaboutcenter',
            old_name='location',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tableaboutcenter',
            old_name='contacts',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tableaboutcenter',
            old_name='email',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tableaboutcenter',
            old_name='worktime',
            new_name='content_4',
        ),
        migrations.RenameField(
            model_name='tablecontacts',
            old_name='name',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tablecontacts',
            old_name='address',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tablecontacts',
            old_name='phone',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tabledepartmentcmr',
            old_name='name',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tabledepartmentcmr',
            old_name='position',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tabledepartmentcmr',
            old_name='worktime',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tabledepartmentcmr',
            old_name='phone',
            new_name='content_4',
        ),
        migrations.RenameField(
            model_name='tabledepartmentdp',
            old_name='name',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tabledepartmentdp',
            old_name='position',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tabledepartmentdp',
            old_name='worktime',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tabledepartmentdp',
            old_name='phone',
            new_name='content_4',
        ),
        migrations.RenameField(
            model_name='tabledepartmentomr',
            old_name='name',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tabledepartmentomr',
            old_name='position',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tabledepartmentomr',
            old_name='worktime',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tabledepartmentomr',
            old_name='phone',
            new_name='content_4',
        ),
        migrations.RenameField(
            model_name='tabledepartmentppp',
            old_name='name',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tabledepartmentppp',
            old_name='position',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tabledepartmentppp',
            old_name='worktime',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tabledepartmentppp',
            old_name='phone',
            new_name='content_4',
        ),
        migrations.RenameField(
            model_name='tabledepartmentst',
            old_name='name',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tabledepartmentst',
            old_name='position',
            new_name='content_2',
        ),
        migrations.RenameField(
            model_name='tabledepartmentst',
            old_name='worktime',
            new_name='content_3',
        ),
        migrations.RenameField(
            model_name='tabledepartmentst',
            old_name='phone',
            new_name='content_4',
        ),
        migrations.RenameField(
            model_name='tableworktime',
            old_name='day',
            new_name='content_1',
        ),
        migrations.RenameField(
            model_name='tableworktime',
            old_name='time',
            new_name='content_2',
        ),
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('text', 'Текст'), ('img', 'Изображение'), ('pdf', 'PDF-файл'), ('map', 'Карта - как пройти'), ('table_horizontal', 'Горизонтальная таблица'), ('table_vertical', 'Вертикальная таблица')], max_length=20, verbose_name='Тип контента'),
        ),
    ]
