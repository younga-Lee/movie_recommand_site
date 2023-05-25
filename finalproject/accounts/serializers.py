from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    followings_cnt = serializers.CharField(source='followings.count', read_only=True)
    followers_cnt = serializers.CharField(source='followers.count', read_only=True)
    
    likes_movies_cnt = serializers.CharField(source='likes_movies.count', read_only=True)
    likes_user_cnt = serializers.CharField(source='likes_user.count', read_only=True)
    
    # followers = serializers.CharField(source='followers', read_only=True)
    
    # 팔로우의 숫자
    # 팔로잉의 숫자
    # follow_count = serializers.IntegerField(source=follower.count)

    class Meta:
        model = User
        # fields = ('username','image', 'followings', 'id')
        fields = '__all__'

        
        
class UserFollowSerailizer(serializers.ModelSerializer):
    followers = UserProfileSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
