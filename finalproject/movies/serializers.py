from rest_framework import serializers
from .models import Movie, Genre, Comment

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('pk','poster_path',)
    

class MovieDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        
class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie')