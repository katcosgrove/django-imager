from django.shortcuts import redirect
from imager_images.models import Album, Photo
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from .forms import PhotoForm, AlbumForm, PhotoEditForm, AlbumEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PhotoCreateView(LoginRequiredMixin, CreateView):
    """Class to add a photo."""

    template_name = 'images/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = '/images/library'
    login_url = reverse_lazy('auth_login')

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


class AlbumCreateView(LoginRequiredMixin, CreateView):
    """Class to add a photo."""

    template_name = 'images/album_create.html'
    model = Album
    form_class = AlbumForm
    success_url = '/images/library'
    login_url = reverse_lazy('auth_login')

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


class PhotoEditView(LoginRequiredMixin, UpdateView):
    """Class to edit a photo."""

    template_name = 'images/photo_edit.html'
    model = Photo
    form_class = PhotoEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('library')

    def get(self, *args, **kwargs):
        """Behavior for get request on photo edit form."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Behavior for post request on photo edit form."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get kwargs from edit form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumEditView(LoginRequiredMixin, UpdateView):
    """Class to edit a album."""

    template_name = 'images/album_edit.html'
    model = Album
    form_class = AlbumEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('library')

    def get(self, *args, **kwargs):
        """Behavior for get request on album edit form."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Behavior for post request on album edit form."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get kwargs from edit form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class LibraryView(LoginRequiredMixin, TemplateView):
    """Class view for library."""

    template_name = 'images/library.html'
    context_object_name = 'library'
    login_url = reverse_lazy('auth_login')

    def get(self, *args, **kwargs):
        """Get username."""
        if kwargs:
            return super().get(*args, **kwargs)

        else:
            kwargs.update({'username': self.request.user.username})
            kwargs.update({'owner': True})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get and return context data for library."""
        context = super().get_context_data(**kwargs)

        photos = Photo.objects.filter(user__username=context['username'])
        albums = Album.objects.filter(user__username=context['username'])

        context['albums'] = albums
        context['photos'] = photos
        return context


class PhotosView(LoginRequiredMixin, ListView):
    """Class view for all public photos."""

    template_name = 'images/photos.html'
    context_object_name = 'photos'
    login_url = reverse_lazy('auth_login')

    def get_queryset(self, **kwargs):
        """Queryset for all public photos."""
        return Photo.objects.filter(published='PUBLIC')


class AlbumsView(LoginRequiredMixin, ListView):
    """Class view for all public albums."""

    template_name = 'images/albums.html'
    context_object_name = 'albums'
    login_url = reverse_lazy('auth_login')

    def get_queryset(self, **kwargs):
        """Queryset for all public albums."""
        return Album.objects.filter(published='PUBLIC')


class PhotoView(LoginRequiredMixin, DetailView):
    """Class view for single photo detail."""

    template_name = 'images/image.html'
    context_object_name = 'photo'
    login_url = reverse_lazy('auth_login')
    model = Photo

    def get_queryset(self, *args, **kwargs):
        """Queryset for single photo."""
        return Photo.objects.filter(id=self.kwargs['pk'])

    def get_object(self, queryset=None):
        """Get the photo object."""
        obj = super(PhotoView, self).get_object(queryset=queryset)
        return obj


class AlbumView(LoginRequiredMixin, DetailView):
    """Class view for single album detail."""

    template_name = 'images/album.html'
    context_object_name = 'album'
    login_url = reverse_lazy('auth_login')
    model = Album

    def get_queryset(self, *args, **kwargs):
        """Queryset for single album."""
        return Album.objects.filter(id=self.kwargs['pk'])

    def get_object(self, queryset=None):
        """Get the album object."""
        obj = super(AlbumView, self).get_object(queryset=queryset)
        return obj
