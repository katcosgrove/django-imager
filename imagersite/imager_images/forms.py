from django.forms import ModelForm
from .models import Photo, Album


class PhotoForm(ModelForm):
    """Class for photo form."""

    class Meta:
        """Metadata for class."""
        model = Photo
        fields = ['image', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Init for class."""
        kwargs.pop('username')
        super().__init__(*args, **kwargs)


class AlbumForm(ModelForm):
    """Class for album form."""

    class Meta:
        model = Album
        fields = ['cover', 'photos', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['cover'].queryset = Photo.objects.filter(user__username =username)
