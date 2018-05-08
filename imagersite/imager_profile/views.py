from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagerProfile
from imager_images.models import Album, Photo
from django.views.generic import TemplateView


# class ProfileView(TemplateView):
#     """
#     Handle profile view for any user.

#     If you are not the owner of the profile, display only public photos and albums.
#     """

#     template_name = 'profile/profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         owner = False

#         if not context.username:
#             username = request.user.get_username()
#             owner = True
#             if username == '':
#                 return redirect('home')

#         profile = get_object_or_404(ImagerProfile, user__username=username)
#         albums = Album.objects.filter(user__username=username)
#         photos = Photo.objects.filter(user__username=username)
#         num_photos_public = len(Photo.objects.filter(user__username=username).filter(published='PUBLIC'))
#         num_albums_public = len(Album.objects.filter(user__username=username).filter(published='PUBLIC'))

#         num_photos_private = len(Photo.objects.filter(user__username=username).filter(published='PRIVATE'))
#         num_albums_private = len(Album.objects.filter(user__username=username).filter(published='PRIVATE'))

#         if not owner:
#             photos = Photo.objects.filter(published='PUBLIC')
#             albums = Album.objects.filter(published='PUBLIC')

#         context['profile'] = profile
#         context['albums'] = albums
#         context['photos'] = photos
#         context['num_albums_public'] = num_albums_public
#         context['num_photos_public'] = num_photos_public
#         context['num_albums_private'] = num_albums_private
#         context['num_photos_private'] = num_photos_private
#         return context


def profile_view(request, username=None):
    """
    Handle profile view for any user.

    If you are not the owner of the profile, display only public photos and albums.
    """
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
