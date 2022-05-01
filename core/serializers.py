from unicodedata import name
from rest_framework import serializers

from .models import Genre, Movie, Serie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        read_only_fields = ['id']
    
    def validate(self, attrs):
        genre = Genre.objects.filter(name=attrs['name']).first()
        if genre:
            raise serializers.ValidationError(detail='Genre with that name already exists!')
        return super().validate(attrs)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'overview', 'imdb_score', 'data_launch', 'genre', 'image']
        read_only_fields = ['id']
    
    def validate(self, attrs):
        movie = Movie.objects.filter(name=attrs['name']).first()
        if movie:
            raise serializers.ValidationError(detail='Movie with that name already exists!')
        return super().validate(attrs)


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'name', 'overview', 'imdb_score', 'data_launch', 'genre', 'image', 'seasons']
        read_only_fields = ['id']

    def validate(self, attrs):
        serie = Serie.objects.filter(name=attrs['name']).first()
        if serie:
            raise serializers.ValidationError(detail='Serie with that name already exists!')
        return super().validate(attrs)
    