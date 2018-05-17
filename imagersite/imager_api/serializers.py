from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    """Serializer for photo endpoint."""

    class Meta:
        """Meta class for photo model."""

        model = Photo
        fields = ('id', 'image', 'title', 'description')


class AlbumSerializer(serializers.ModelSerializer):
    """Serializer for album endpoint."""

    class Meta:
        """Meta class for album model."""

        model = Album
        fields = ('id', 'cover', 'photos', 'title', 'description')
