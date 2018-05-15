from rest_framework import generics
from .serializers import PhotoSerializer, AlbumSerializer
from imager_images.models import Photo, Album


class PhotoListAPI(generics.ListAPIView):
    """View for API list of all photos."""

    serializer_class = PhotoSerializer

    def get_queryset(self):
        """Queryset including filter of photo objects for current user."""
        return Photo.objects.filter(user=self.request.user)


class AlbumListAPI(generics.ListAPIView):
    """View for API list of all photos."""

    serializer_class = AlbumSerializer

    def get_queryset(self):
        """Queryset including filter of album objects for current user."""
        return Album.objects.filter(user=self.request.user)
