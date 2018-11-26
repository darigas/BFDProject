# Generated by Django 2.1.3 on 2018-11-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_watchlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movie.Movie'),
        ),
    ]