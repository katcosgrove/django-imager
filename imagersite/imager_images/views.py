from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from imager_profile.models import ImagerProfile

# Create your views here.


def library_view(request, username=None):
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

    # import pdb; pdb.set_trace()

    return render(request, 'images/library.html', context)
