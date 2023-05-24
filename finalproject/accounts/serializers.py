from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','image', 'followings', 'id')
        # fields = '__all__'
        
        
class UserFollowSerailizer(serializers.ModelSerializer):
    followers = UserProfileSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'


# class UserLikeSerializer(serializers.ModelSerializer):
#     movie_set = (many=True, read_only=True)
#     class Meta:
#         model = Movie
#         fields = '__all__'
        