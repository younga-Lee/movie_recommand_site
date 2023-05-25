from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated #로그인 해야만 가능
from .models import User
from .serializers import UserProfileSerializer

User = get_user_model()
#유저
@api_view(['GET'])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)   

#유저 수정
@api_view(['PUT', 'GET'])
def user_edit(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    
#팔로우, 팔로워
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    me = request.user
    if person != me:
        if person.followers.filter(username=me.username).exists():
            person.followers.remove(me)
            followed = False
        else:
            person.followers.add(me)
            followed = True
        return Response(followed)

#위시리스트
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_id):
    user = request.user
    if user.likes_movies.filter(id=movie_id).exists():
        user.likes_movies.remove(movie_id)
        liked = False
    else:
        user.likes_movies.add(movie_id)
        liked = True
    return Response(liked)
