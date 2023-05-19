from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'poster',)
        

class MovieDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        moidel = Movie
        fields = '__all__'