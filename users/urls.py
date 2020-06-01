from django.urls import path
from .views import CreateUserView, DetailUserView, UpdateUserView


urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    path('profile/<int:pk>/', DetailUserView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', UpdateUserView.as_view(), name="update_user")
]