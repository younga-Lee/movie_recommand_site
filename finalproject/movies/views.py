from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated #로그인 해야만 가능

from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

def movie_create(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return Response(serializer.data)