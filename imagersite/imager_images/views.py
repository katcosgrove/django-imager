from django.shortcuts import redirect
from imager_images.models import Album, Photo
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .forms import PhotoForm, AlbumForm


class PhotoCreateView(CreateView):
    """Class to add a photo."""

    template_name = 'images/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = '/images/library'

    def get(self, *args, **kwargs):
        """On get request, redirect home if user is not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """On post request, redirect home if user is not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get keyword arguments from form and add username."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumCreateView(CreateView):
    """Class to add a photo."""

    template_name = 'images/album_create.html'
    model = Album
    form_class = AlbumForm
    success_url = '/images/library'

    def get(self, *args, **kwargs):
        """On get request, redirect home if user is not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """On post request, redirect home if user is not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get keyword arguments from form and add username."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class LibraryView(TemplateView):
    """Class view for library."""
    template_name = 'images/library.html'
    context_object_name = 'library'

    def get(self, *args, **kwargs):
        """Get authenticated user and redirect if not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get and return context data for library."""
        context = super().get_context_data(**kwargs)

        photos = Photo.objects.filter(published='PUBLIC')
        albums = Album.objects.filter(published='PUBLIC')

        context['albums'] = albums
        context['photos'] = photos
        return context


class PhotosView(ListView):
    """Class view for all public photos."""

    template_name = 'images/photos.html'
    context_object_name = 'photos'

    def get(self, *args, **kwargs):
        """Get authenticated user and redirect if not authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self, **kwargs):
        """Queryset for all public photos."""
        return Photo.objects.filter(published='PUBLIC')


class AlbumsView(ListView):
    """Class view for all public albums."""

    template_name = 'images/albums.html'
    context_object_name = 'albums'

    def get(self, *args, **kwargs):
        """Check if user is authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self, **kwargs):
        """Queryset for all public albums."""
        return Album.objects.filter(published='PUBLIC')


class PhotoView(DetailView):
    """Class view for single photo detail."""

    template_name = 'images/image.html'
    context_object_name = 'photo'
    model = Photo

    def get(self, *args, **kwargs):
        """Check if user is authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """Queryset for single photo."""
        return Photo.objects.filter(id=self.kwargs['pk'])

    def get_object(self, queryset=None):
        """Get the photo object."""
        obj = super(PhotoView, self).get_object(queryset=queryset)
        return obj


class AlbumView(DetailView):
    """Class view for single album detail."""

    template_name = 'images/album.html'
    context_object_name = 'album'
    model = Album

    def get(self, *args, **kwargs):
        """Check if user is authenticated."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """Queryset for single album."""
        return Album.objects.filter(id=self.kwargs['pk'])

    def get_object(self, queryset=None):
        """Get the album object."""
        obj = super(AlbumView, self).get_object(queryset=queryset)
        return obj
