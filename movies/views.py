import datetime
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CinemasSerializer,
    MovieFormatSerializer,
    MovieSerializer,
    RoomsFormatSerializer,
    RoomsSerializer,
    ShowTimeSerializer
)

from .models import (
    Cinemas,
    MovieFormat,
    Movie,
    RoomsFormat,
    Rooms,
    ShowTime,
)

from users.permissions import IsAdminOrReadOnly


class CinemasViewSet(ModelViewSet):
    serializer_class = CinemasSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Cinemas.objects.all()


class MovieFormatViewSet(ModelViewSet):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = RoomsFormat.objects.all()


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Movie.objects.filter(ending_of_movie__gt=datetime.datetime.now())


class RoomsFormatViewSet(ModelViewSet):
    serializer_class = RoomsFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = RoomsFormat.objects.all()


class RoomsViewSet(ModelViewSet):
    serializer_class = RoomsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Rooms.objects.all()


class ShowTimeViewSet(ModelViewSet):
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ShowTime.objects.filter(is_active=True)
