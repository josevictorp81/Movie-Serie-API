from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Movie, Serie
from .serializers import GenreSerializer, MovieSerializer, SerieSerializer, ReadMovieSerializer, ReadSerieSerializer


class GenreViewSet(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class MovieViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = self.queryset.filter(name__icontains=name)
            serializer = ReadMovieSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return super().list(request, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadMovieSerializer
        return self.serializer_class


class SerieViewSet(ListModelMixin ,CreateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SerieSerializer
    queryset = Serie.objects.all()

    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = self.queryset.filter(name__icontains=name)
            serializer = ReadSerieSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadSerieSerializer
        return self.serializer_class
