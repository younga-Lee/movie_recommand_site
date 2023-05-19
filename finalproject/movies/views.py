from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated #로그인 해야만 가능

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


# #전체 영화 리스트 
# @api_view(['GET'])
# def movie_list(request):
#     movies = get_list_or_404(Movie)
#     serializer = MovieListSerializer(movies, many=True)
#     return Response(serializer.data)

# #영화 하나의 상세정보
# @api_view(['GET'])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieDetailSerializer(Movie)
#     print(serializer.data)
#     return Response(serializer.data)
    

    


    