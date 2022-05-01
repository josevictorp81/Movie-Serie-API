from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.serializers import ValidationError

from core.models import Genre, Serie
from core.serializers import SerieSerializer

SERIE_URL = reverse('serie-list')

def detail_url(serie_id):
    return reverse('serie-detail', args=[serie_id])

def create_genre(name='Ação'):
    return Genre.objects.create(name=name)

class SerieTest(APITestCase):
    def setUp(self) -> None:
        self.cliente = APIClient()
        
    def test_create_serie(self):
        genre1 = create_genre()
        genre2 = create_genre(name='Animação')
        payload = {'name': 'serie', 'overview': 'testando', 'imdb_score': 8.7, 'data_launch': '2022-04-03', 'genre': [genre1.id, genre2.id], 'seasons': 2}
        res = self.client.post(SERIE_URL, payload)

        serie = Serie.objects.get(id=res.data['id'])
        serializer = SerieSerializer(serie)
        genres = serie.genre.all()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, serializer.data)
        self.assertIn(genre1, genres)
        self.assertIn(genre2, genres)
        self.assertEqual(genres.count(), 2)        
    
    def test_create_serie_exists(self):
        genre = create_genre(name='Animação')
        serie = Serie.objects.create(name='serie', imdb_score=8.7, data_launch='2022-03-23')
        serie.genre.add(genre.id)
        serie2 = {'name': 'serie', 'imdb_score': 8.7, 'data_launch': '2022-03-23', 'genre': [genre.id]}

        with self.assertRaisesMessage(ValidationError, 'Serie with that name already exists!'):
            serializer = SerieSerializer(data=serie2)
            serializer.is_valid(raise_exception=True)
    
    def test_list_serie(self):
        genre = create_genre(name='Animação')
        serie = Serie.objects.create(name='serie', imdb_score=8.7, data_launch='2022-03-23')
        serie.genre.add(genre.id)

        res = self.client.get(SERIE_URL)

        series = Serie.objects.all()
        serializer = SerieSerializer(series ,many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_list_filter_serie(self):
        genre = create_genre()
        serie1 = Serie.objects.create(name='test', imdb_score=8.7, data_launch='2022-03-23')
        serie1.genre.add(genre.id)
        serie2 = Serie.objects.create(name='serie 2', imdb_score=8.7, data_launch='2022-03-23', seasons=4)
        serie2.genre.add(genre.id)
        serie3 = Serie.objects.create(name='serie 3', imdb_score=8.7, data_launch='2022-03-23')
        serie3.genre.add(genre.id)

        res = self.client.get(SERIE_URL, {'name': 'serie'})

        series = Serie.objects.filter(name__icontains='serie')
        serializer = SerieSerializer(series, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(serializer.data))
    
    def test_list_serie_detail(self):
        genre = create_genre()
        serie = Serie.objects.create(name='test', imdb_score=8.7, data_launch='2022-03-23', seasons=4)
        serie.genre.add(genre.id)

        url = detail_url(serie.id)
        res = self.client.get(url)
        serializer = SerieSerializer(serie)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    