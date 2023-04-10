# Generated by Django 4.2 on 2023-04-09 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_menu_related_list_of_purchased_games_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='activate_this_menu_on_link',
            field=models.ManyToManyField(blank=True, related_name='included_id', to='main.category', verbose_name='Список статей'),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='included_categories',
        ),
        migrations.AddField(
            model_name='menu',
            name='included_categories',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Foreinkey'),
            preserve_default=False,
        ),
    ]
