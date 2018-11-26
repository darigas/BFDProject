from django.db import models
import datetime
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):YEAR_CHOICES.append((r, r))
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField('Movie', related_name='movie_set', blank=True)

    def __str__(self):
        return self.user.username