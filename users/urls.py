from django.urls import url
from .views import CreateUserView, DetailUserView, UpdateUserView


urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name="register"),
    url(r'^profile/<int:pk>/', DetailUserView.as_view(), name='profile'),
    url(r'^profile/<int:pk>/edit/', UpdateUserView.as_view(), name="update_user")
]

f settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)