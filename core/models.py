from django.db import models
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('images/', filename)

class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Genres'
    
    def __str__(self) -> str:
        return self.name


class Base(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    imdb_score = models.FloatField()
    data_launch = models.DateField()
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(blank=True, upload_to=get_file_path)

    def __str__(self) -> str:
        return self.name
        

class Movie(Base):

    class Meta:
        verbose_name_plural = 'Movies'


class Serie(Base):
    seasons = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Series'
        