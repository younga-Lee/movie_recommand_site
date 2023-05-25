from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='media/', blank=True, default='profile.svg')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    likes_movies = models.ManyToManyField('movies.Movie', related_name='likes_user')
    