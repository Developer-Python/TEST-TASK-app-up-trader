# Generated by Django 4.2 on 2023-04-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_menu_activate_this_menu_on_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='activate_this_menu_on_link',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='included_categories',
        ),
        migrations.AddField(
            model_name='menu',
            name='included_categories',
            field=models.ManyToManyField(blank=True, related_name='included_categories', to='main.category', verbose_name='Список категорий в данном меню'),
        ),
    ]
