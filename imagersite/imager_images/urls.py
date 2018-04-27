from django.urls import path
from .views import library_view, photos_view, albums_view, photo_view, album_view


urlpatterns = [
    path('', library_view, name='library'),
    path('photos/', photos_view, name='photos'),
    path('photos/<str:photo_id>', photo_view, name='photo'),
    path('albums/', albums_view, name='albums'),
    path('albums/<str:album_id>', album_view, name='album'),

]
