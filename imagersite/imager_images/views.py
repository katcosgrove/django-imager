from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from imager_profile.models import ImagerProfile
from django.views.generic import ListView, CreateView, DetailView
from .forms import PhotoForm
# from django.conf import settings


class PhotoCreateView(CreateView):
    """Class to add a photo."""

    template_name = 'images/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = 'photos'

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


# class LibraryView(ListView):
#     template_name = 'images/library.html'
#     context_object_name = 'library'

#     def get_queryset(self):
#         # profile = get_object_or_404(ImagerProfile, user__username=username)
#         albums = Album.objects.filter(published='PUBLIC')
#         photos = Photo.objects.filter(published='PUBLIC')
#         return {
#             # 'profile': profile,
#             'albums': albums,
#             'photos': photos,
#         }

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['library'] = self.get_queryset
#         context['cover'] = settings.STATIC_URL + 'default_cover.thumbnail'


class PhotosView(ListView):
    """Class view for all public photos."""

    template_name = 'images/photos.html'
    context_object_name = 'photos'

    def get(self, *args, **kwargs):
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


def library_view(request, username=None):
    """Display all public photos and albums."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Album.objects.filter(user__username=username)
    photos = Photo.objects.filter(user__username=username)

    if not owner:
        photos = Photo.objects.filter(published='PUBLIC')
        albums = Album.objects.filter(published='PUBLIC')

    context = {
        'profile': profile,
        'albums': albums,
        'photos': photos,
    }

    return render(request, 'images/library.html', context)


def album_view(request, username=None, album_id=None):
    """
    Display details about a particular album.

    If you are that user, display all photos in that album.
    If not, display only public photos in that album.
    """
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    album = Album.objects.filter(id=album_id).first()

    if not owner:
        album = Album.objects.filter(id=album_id).filter(published='PUBLIC')

    context = {
        'album': album,
    }
    # import pdb; pdb.set_trace()
    return render(request, 'images/album.html', context)
