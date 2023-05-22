from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('pk','poster_path',)
    

class MovieDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        moidel = Movie
        fields = '__all__'