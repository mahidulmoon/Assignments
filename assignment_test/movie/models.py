from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=15)
    rating = models.CharField(max_length=15)
    release_date = models.CharField(max_length=15)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie_id=self)
        for rating in ratings:
            sum += rating.rating
        
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0




class Rating(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='+')
    rating = models.DecimalField(max_digits=2,decimal_places=1,validators=[
        MinValueValidator(1),MaxValueValidator(5)
    ])