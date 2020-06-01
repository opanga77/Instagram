from django.urls import url
from .views import PostListView, PostCreateView


urlpatterns = [
    url(r'', PostListView.as_view(), name='home'),
    url(r'^create/',PostCreateView.as_view(), name='create_post' )
]

f settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)