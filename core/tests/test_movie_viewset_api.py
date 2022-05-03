from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.serializers import ValidationError

from core.models import Genre, Movie
from core.serializers import MovieSerializer, ReadMovieSerializer

MOVIE_URL = reverse('movie-list')

def detail_url(movie_id):
    return reverse('movie-detail', args=[movie_id])

def create_genre(name='Ação'):
    return Genre.objects.create(name=name)

class MovieTests(APITestCase):
    def setUp(self) -> None:
        self.cliente = APIClient()

    def test_create_movie(self):
        genre1 = create_genre()
        genre2 = create_genre(name='Animação')
        payload = {'name': 'movie1', 'overview': 'testando', 'imdb_score': 6.9, 'data_launch': '2022-04-03', 'genre': [genre1.id, genre2.id]}
        res = self.client.post(MOVIE_URL, payload)

        movie = Movie.objects.get(id=res.data['id'])
        serializer = MovieSerializer(movie)
        genres = movie.genre.all()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, serializer.data)
        self.assertIn(genre1, genres)
        self.assertIn(genre2, genres)
        self.assertEqual(genres.count(), 2)
    
    def test_create_movie_exists(self):
        genre = create_genre(name='Animação')
        movie = Movie.objects.create(name='movie', imdb_score=8.7, data_launch='2022-03-23')
        movie.genre.add(genre.id)
        movie2 = {'name': 'movie', 'imdb_score': 8.7, 'data_launch': '2022-03-23', 'genre': [genre.id]}

        with self.assertRaisesMessage(ValidationError, 'Movie with that name already exists!'):
            serializer = MovieSerializer(data=movie2)
            serializer.is_valid(raise_exception=True)
    
    def test_list_movie(self):
        genre = create_genre(name='Animação')
        movie = Movie.objects.create(name='movie', imdb_score=8.7, data_launch='2022-03-23')
        movie.genre.add(genre.id)

        res = self.client.get(MOVIE_URL)

        movie = Movie.objects.all()
        serializer = ReadMovieSerializer(movie, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_list_filter_movie(self):
        genre = create_genre()
        movie1 = Movie.objects.create(name='test', imdb_score=8.7, data_launch='2022-03-23')
        movie1.genre.add(genre.id)
        movie2 = Movie.objects.create(name='movie', imdb_score=8.7, data_launch='2022-03-23')
        movie2.genre.add(genre.id)
        movie3 = Movie.objects.create(name='movie test', imdb_score=8.7, data_launch='2022-03-23')
        movie3.genre.add(genre.id)

        res = self.client.get(MOVIE_URL, {'name': 'movie'})

        movies = Movie.objects.filter(name__icontains='movie')
        serializer = ReadMovieSerializer(movies, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_list_movie_detail(self):
        genre = create_genre()
        movie = Movie.objects.create(name='test', imdb_score=8.7, data_launch='2022-03-23')
        movie.genre.add(genre.id)

        url = detail_url(movie.id)
        res = self.client.get(url)
        serializer = ReadMovieSerializer(movie)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        