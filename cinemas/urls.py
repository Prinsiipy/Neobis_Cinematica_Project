from django.urls import path, include
from rest_framework import routers
from .views import CinemaViewSet

from .views import (
    RoomList, RoomDetail,
    SeatList, SeatDetail,
)
router = routers.DefaultRouter()
router.register(r'cinemas', CinemaViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('rooms/', RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),

    path('seats/', SeatList.as_view(), name='seat-list'),
    path('seats/<int:pk>/', SeatDetail.as_view(), name='seat-detail'),
]

