from django.urls import path
from rest_framework.authtoken import views
from .views import PhotoListAPI, AlbumListAPI


urlpatterns = [
    path('photo/', PhotoListAPI.as_view(), name='photo_list_api'),
    path('album/', AlbumListAPI.as_view(), name='album_list_api'),
    path('auth-token-login/', views.obtain_auth_token)
]
