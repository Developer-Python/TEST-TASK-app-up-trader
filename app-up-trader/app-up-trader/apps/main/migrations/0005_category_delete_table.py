# Generated by Django 4.2 on 2023-04-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_autoupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название категорий')),
                ('discription', models.CharField(max_length=50, verbose_name='Ссылка категорий')),
            ],
            options={
                'verbose_name': 'Новая категория',
                'verbose_name_plural': '1) Категории',
            },
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
