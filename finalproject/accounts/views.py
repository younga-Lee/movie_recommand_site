from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated #로그인 해야만 가능
from .models import User
from .serializers import UserProfileSerializer

User = get_user_model()
# Create your views here.
@api_view(['GET'])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)   

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
    
@api_view(['PUT'])
def user_edit(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    