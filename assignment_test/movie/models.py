from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=15)
    rating = models.CharField(max_length=15)
    release_date = models.CharField(max_length=15)