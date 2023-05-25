from django.db import models
from django.conf import settings

class Genre(models.Model) :
    name = models.CharField(max_length=50)

class Movie(models.Model) : 
    title = models.CharField(max_length=100)
    overview = models.TextField()
    adult = models.BooleanField()
    poster_path = models.TextField()
    backdrop_path = models.TextField(null=True, default=None)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    runtime = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) 
    comment_content = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    
    