from django.db import models

# Create your models here.
class Movie(models.Model) : 
    title = models.TextField()
    overview = models.TextField()
    adult = models.BooleanField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    runtime = models.FloatField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment_content = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    #user_id