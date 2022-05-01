from django.contrib import admin

from .models import Serie, Movie, Genre

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'data_launch']
    list_editable = ['imdb_score', 'data_launch']


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'data_launch']
    list_editable = ['imdb_score', 'data_launch']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
