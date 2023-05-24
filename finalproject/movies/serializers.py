from rest_framework import serializers
from .models import Movie, Genre, Comment

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('pk','poster_path',)
    
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user')

class MovieDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        
class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'
