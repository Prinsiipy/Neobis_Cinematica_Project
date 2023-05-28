from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import (
    CinemasViewSet,
    MovieViewSet,
    RoomsFormatViewSet,
    RoomsViewSet,
    MovieFormatViewSet,
    ShowTimeViewSet
)

movies_router = DefaultRouter()
movies_router.register(r'movies', CinemasViewSet, basename='movies')
movies_router.register(r'movies', MovieViewSet, basename='movies')
movies_router.register(r'rooms-format', RoomsFormatViewSet, basename='rooms-format')
movies_router.register(r'rooms', RoomsViewSet, basename='rooms')
movies_router.register(r'movie-format', MovieFormatViewSet, basename='movie-format')
movies_router.register(r'showtime', ShowTimeViewSet, basename='showtime')

urlpatterns = [
]