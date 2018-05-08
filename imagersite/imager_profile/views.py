from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagerProfile
from imager_images.models import Album, Photo
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """
    Handle profile view for any user.

    If you are not the owner of the profile, display only public photos and albums.
    """

    template_name = 'profile/profile.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        
        kwargs.update({'username': self.request.user.username})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = False

        if not context['username']:
            context['username'] = request.user.get_username()
            owner = True

        profile = get_object_or_404(ImagerProfile, user__username=context['username'])
        albums = Album.objects.filter(user__username=context['username'])
        photos = Photo.objects.filter(user__username=context['username'])
        num_photos_public = len(Photo.objects.filter(user__username=context['username']).filter(published='PUBLIC'))
        num_albums_public = len(Album.objects.filter(user__username=context['username']).filter(published='PUBLIC'))

        num_photos_private = len(Photo.objects.filter(user__username=context['username']).filter(published='PRIVATE'))
        num_albums_private = len(Album.objects.filter(user__username=context['username']).filter(published='PRIVATE'))

        if not owner:
            photos = Photo.objects.filter(published='PUBLIC')
            albums = Album.objects.filter(published='PUBLIC')

        context['profile'] = profile
        context['albums'] = albums
        context['photos'] = photos
        context['num_albums_public'] = num_albums_public
        context['num_photos_public'] = num_photos_public
        context['num_albums_private'] = num_albums_private
        context['num_photos_private'] = num_photos_private
        return context
