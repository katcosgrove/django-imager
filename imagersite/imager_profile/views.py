from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagerProfile
from imager_images.models import Album, Photo
# Create your views here.


def profile_view(request, username=None):
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Album.objects.filter(user__username=username)
    photos = Photo.objects.filter(user__username=username)
    num_photos_public = len(Photo.objects.filter(user__username=username).filter(published='PUBLIC'))
    num_albums_public = len(Album.objects.filter(user__username=username).filter(published='PUBLIC'))

    num_photos_private = len(Photo.objects.filter(user__username=username).filter(published='PRIVATE'))
    num_albums_private = len(Album.objects.filter(user__username=username).filter(published='PRIVATE'))

    if not owner:
        photos = Photo.objects.filter(published='PUBLIC')
        albums = Album.objects.filter(published='PUBLIC')

    context = {
        'profile': profile,
        'albums': albums,
        'photos': photos,
        'num_albums_public': num_albums_public,
        'num_photos_public': num_photos_public,
        'num_albums_private': num_albums_private,
        'num_photos_private': num_photos_private,
    }

    return render(request, 'profile/profile.html', context)
