from django.contrib.auth.models import User
from django.db import models
import datetime

YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class Show(models.Model):
    title = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    season_num = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.title, self.id)


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shows = models.ManyToManyField(Show, related_name='actors')







