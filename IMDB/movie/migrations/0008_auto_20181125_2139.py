# Generated by Django 2.1.3 on 2018-11-25 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0007_auto_20181125_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='movie_set', to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='profile',
            name='watch_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to='movie.WatchList'),
        ),
    ]
