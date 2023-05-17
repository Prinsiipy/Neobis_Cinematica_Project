from django.urls import path
from .views import CustomTokenObtainPairView, register

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', register, name='register'),
]
