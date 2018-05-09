from django.urls import path
from .views import LibraryView, PhotosView, AlbumsView, PhotoView, AlbumView, PhotoCreateView, AlbumCreateView


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('photos/<int:pk>', PhotoView.as_view(), name='photo'),
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('albums/<int:pk>', AlbumView.as_view(), name='album'),
    path('photos/add', PhotoCreateView.as_view(), name='photo_create'),
    path('albums/add', AlbumCreateView.as_view(), name='album_create')
]
