from django.urls import path
from .views import library_view, photos_view, albums_view, photo_view, album_view, PhotoCreateView


urlpatterns = [
    path('library/', library_view, name='library'),
    path('photos/', photos_view, name='photos'),
    path('photos/<int:photo_id>', photo_view, name='photo'),
    path('albums/', albums_view, name='albums'),
    path('albums/<int:album_id>', album_view, name='album'),
    path('photos/add', PhotoCreateView.as_view(), name='photo_create')
]
