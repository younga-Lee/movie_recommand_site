from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated #로그인 해야만 가능
from .models import User
from .serializers import UserProfileSerializer

# Create your views here.
@api_view(['GET'])
def user_detail(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)   
