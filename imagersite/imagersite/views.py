from imager_images.models import Photo
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """View class for the homepage."""

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """Get request for homepage class view."""
        context = super().get_context_data(**kwargs)
        try:
            random_image = Photo.objects.filter(published='PUBLIC').order_by('?')[0]
            random_image = random_image.image
            context['image'] = random_image.url
            return context
        except IndexError:
            random_image = '/static/birdcage.jpg'
            context['image'] = random_image.url
            return context
