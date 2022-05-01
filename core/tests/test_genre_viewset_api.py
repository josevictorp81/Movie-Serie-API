from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.serializers import ValidationError

from core.models import Genre
from core.serializers import GenreSerializer

GENRE_URL = reverse('genre-list')

def create_genre(name='Ação'):
    return Genre.objects.create(name=name)

class GenreTests(APITestCase):
    def setUp(self) -> None:
        self.cliente = APIClient()
    
    def test_list_genre(self):
        create_genre()
        create_genre(name='Aventura')

        res = self.client.get(GENRE_URL)

        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_create_genre(self):
        payload = {'name': 'Ação'}
        res = self.client.post(GENRE_URL, payload)
        genre = Genre.objects.filter(name=payload['name']).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(genre)
    
    def test_create_genre_exists(self):
        create_genre()
        genre = {'name': 'Ação'}

        with self.assertRaisesMessage(ValidationError, 'Genre with that name already exists!'):
            serializer = GenreSerializer(data=genre)
            serializer.is_valid(raise_exception=True)
        