# Generated by Django 2.1.3 on 2018-11-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20181125_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='watch_list',
        ),
        migrations.AddField(
            model_name='profile',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='movie_set', to='movie.Movie'),
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]
