from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','image',)
        
        
class UserFollowSerailizer(serializers.ModelSerializer):
    followers = UserProfileSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'