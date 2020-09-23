from rest_framework import serializers
from rest_framework.response import Response
from .models import Movie,Rating



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= ['name','genre','rating','release_date','avg_rating']
        


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields= "__all__"
        