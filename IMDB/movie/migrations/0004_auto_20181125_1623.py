# Generated by Django 2.1.3 on 2018-11-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20181125_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='movies',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.Movie'),
        ),
    ]
