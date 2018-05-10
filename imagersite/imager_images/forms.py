from django.forms import ModelForm
from .models import Photo, Album
from django.forms import ModelForm, CharField, widgets


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
        """Metadata for class."""

        model = Album
        fields = ['cover', 'photos', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Initialize class forms."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['cover'].queryset = Photo.objects.filter(user__username=username)


class PhotoEditForm(ModelForm):
    """Form to edit photo information."""

    class Meta:
        """Metadata for class."""

        model = Photo
        fields = ['title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Initialize class forms."""
        kwargs.pop('username')
        super().__init__(*args, **kwargs)


class AlbumEditForm(ModelForm):
    """Form to edit album information."""

    class Meta:
        """Metadata for class."""

        model = Album
        fields = ['cover', 'photos', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Initialize class forms."""
        kwargs.pop('username')
        super().__init__(*args, **kwargs)
