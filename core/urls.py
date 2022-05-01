from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('genres', views.GenreViewSet)
router.register('movies', views.MovieViewSet)
router.register('series', views.SerieViewSet)

urlpatterns = [
    path('', include(router.urls))
]