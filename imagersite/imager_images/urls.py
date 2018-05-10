from django.urls import path
from .views import LibraryView, PhotosView, AlbumsView, PhotoView, AlbumView
from .views import PhotoCreateView, AlbumCreateView, PhotoEditView, AlbumEditView


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('photos/<int:pk>', PhotoView.as_view(), name='photo'),
    path('photos/<int:pk>/edit', PhotoEditView.as_view(), name='photo_edit'),
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('albums/<int:pk>', AlbumView.as_view(), name='album'),
    path('albums/<int:pk>/edit', AlbumEditView.as_view(), name='album_edit'),
    path('photos/add', PhotoCreateView.as_view(), name='photo_create'),
    path('albums/add', AlbumCreateView.as_view(), name='album_create')
]
