from django.urls import path
from .views import library_view, PhotosView, AlbumsView, PhotoView, album_view, PhotoCreateView


urlpatterns = [
    path('library/', library_view, name='library'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('photos/<int:pk>', PhotoView.as_view(), name='photo'),
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('albums/<int:album_id>', album_view, name='album'),
    path('photos/add', PhotoCreateView.as_view(), name='photo_create')
]
