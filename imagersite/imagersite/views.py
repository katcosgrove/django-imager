from django.shortcuts import render
from imager_images.models import Photo


def home_view(request):
    """Return home view."""

    random_image = Photo.objects.filter(published='PUBLIC').order_by('?')[0]
    random_image = random_image.image
    # import pdb; pdb.set_trace()
    return render(request, 'home.html', {'image': random_image.url})
