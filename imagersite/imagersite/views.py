from django.shortcuts import render
from imager_images.models import Photo


def home_view(request):
    """Return home view."""
    try:
        random_image = Photo.objects.filter(published='PUBLIC').order_by('?')[0]
        random_image = random_image.image
        return render(request, 'home.html', {'image': random_image.url})
    except IndexError:
        random_image = '/static/birdcage.jpg'
        return render(request, 'home.html', {'image': random_image})
