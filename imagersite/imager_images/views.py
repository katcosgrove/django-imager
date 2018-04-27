from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from imager_profile.models import ImagerProfile

# Create your views here.


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


def photos_view(request, username=None):
    """Display all photos for a particular user."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    photos = Photo.objects.filter(user__username=username)

    if not owner:
        photos = Photo.objects.filter(published='PUBLIC')

    context = {
        'photos': photos,
    }

    return render(request, 'images/photos.html', context)


def photo_view(request, photo_id=None):
    """Display details about a single photo."""

    photo = Photo.objects.filter(id=photo_id)
    # import pdb; pdb.set_trace()
    context = {
        'photo': photo[0],
    }
    return render(request, 'images/image.html', context)


def albums_view(request, username=None):
    """Display all albums for a specific user."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    albums = Album.objects.filter(user__username=username)

    if not owner:
        albums = Album.objects.filter(published='PUBLIC')

    context = {
        'albums': albums,
    }

    return render(request, 'images/albums.html', context)


def album_view(request, album_id=None):
    """Display details about a particular album."""

    photos = Photo.objects.filter(albums=album_id).filter(published='PUBLIC')

    context = {
        'photos': photos,
    }

    return render(request, 'images/album.html', context)
