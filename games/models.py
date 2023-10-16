from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title
