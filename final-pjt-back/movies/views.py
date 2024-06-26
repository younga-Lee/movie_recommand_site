from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter

from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated #로그인 해야만 가능

from .models import Movie, Genre, Comment
from .serializers import MovieListSerializer, MovieDetailSerializer, GenreListSerializer, CommentSerializer
import random

#전체 영화 리스트 
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

#영화 검색(제목)
@api_view(['GET'])
def search(request):
    search_query = request.query_params.get('query', '') #검색어
    movies = Movie.objects.filter(title__icontains=search_query)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


#영화 하나의 상세정보
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

#런타임, 장르에 따른 검색어
@api_view(['GET'])
def filter_movies(request):
    runtime_query = request.query_params.get('runtime', '') # 런타임(파라미터명도 runtime으로 하면됨)
    genre_query = request.query_params.get('genre', '') # 장르
    adult_query = request.query_params.get('adult', '') # 성인

    movies = Movie.objects.all()

    if runtime_query:
        movies = movies.filter(runtime__lte=runtime_query)
    if genre_query:
        movies = movies.filter(genres__name__icontains=genre_query)
    if adult_query == 'true':
            movies = movies.filter(adult=True)
    elif adult_query == 'false':
        movies = movies.filter(adult=False)

    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 한줄평 목록 조회
@api_view(['GET'])
def comment_list(request, movie_id):
    comments = get_list_or_404(Comment, movie=movie_id)
    serializer = CommentSerializer(comments, many=True)
    # print(serializer.data)
    return Response(serializer.data)


#한줄평 작성
@api_view(['POST'])
def comment_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

# 한줄평 디테일
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, movie_id, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
