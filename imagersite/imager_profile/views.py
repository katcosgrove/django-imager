from django.shortcuts import get_object_or_404
from .models import ImagerProfile
from .forms import ProfileEditForm
from imager_images.models import Album, Photo
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    Handle profile view for any user.

    If you are not the owner of the profile, display only public photos and albums.
    """

    template_name = 'profile/profile.html'
    login_url = reverse_lazy('auth_login')

    def get(self, *args, **kwargs):
        """Get username."""
        if kwargs:
            return super().get(*args, **kwargs)

        else:
            kwargs.update({'username': self.request.user.username})
            # kwargs.update({'owner': True})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get context data for profiles."""
        context = super().get_context_data(**kwargs)

        profile = get_object_or_404(ImagerProfile, user__username=context['username'])
        albums = Album.objects.filter(user__username=context['username'])
        photos = Photo.objects.filter(user__username=context['username'])
        num_photos_public = len(Photo.objects.filter(user__username=context['username']).filter(published='PUBLIC'))
        num_albums_public = len(Album.objects.filter(user__username=context['username']).filter(published='PUBLIC'))

        num_photos_private = len(Photo.objects.filter(user__username=context['username']).filter(published='PRIVATE'))
        num_albums_private = len(Album.objects.filter(user__username=context['username']).filter(published='PRIVATE'))

        if context['username'] != self.request.user.username:
            photos = photos.filter(published='PUBLIC')
            albums = albums.filter(published='PUBLIC')

        context['profile'] = profile
        context['albums'] = albums
        context['photos'] = photos
        context['num_albums_public'] = num_albums_public
        context['num_photos_public'] = num_photos_public
        context['num_albums_private'] = num_albums_private
        context['num_photos_private'] = num_photos_private
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Class for view to edit profile information."""

    template_name = 'profile/edit_profile.html'
    model = ImagerProfile
    form_class = ProfileEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('profile')
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    def get(self, *args, **kwargs):
        """Behavior for get request on profile edit form."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Behavior for post request on profile edit form."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get kwargs from edit form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user.email = form.data['email']
        form.instance.user.email = form.data['first_name']
        form.instance.user.email = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)
