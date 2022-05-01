from rest_framework.test import APITestCase
from core.models import Genre, Movie, Serie, get_file_path
import uuid

def create_genre(name='Ação'):
    return Genre.objects.create(name=name)

class ModelTest(APITestCase):
    def setUp(self) -> None:
            self.filename = f'images/{uuid.uuid4()}.jpg'

    def test_genre_str(self):
        genre = create_genre()

        self.assertEqual(genre.__str__(), 'Ação')
    
    def test_movie_str(self):
        genre = create_genre()
        movie = Movie.objects.create(name='movie', imdb_score=8.7, data_launch='2022-03-23')
        movie.genre.add(genre.id)

        self.assertEqual(movie.__str__(), 'movie')
    
    def test_serie_str(self):
        genre = create_genre()
        serie = Serie.objects.create(name='serie', imdb_score=9, data_launch='2022-03-23')
        serie.genre.add(genre.id)

        self.assertEqual(serie.__str__(), 'serie')
    
    def test_get_file_path(self):
        file = get_file_path(None, 'test.jpg')

        self.assertEqual(len(self.filename), len(file))
