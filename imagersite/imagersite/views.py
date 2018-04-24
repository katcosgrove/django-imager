from django.shortcuts import render


def home_view(request):
    """Return home view."""
    return render(request, 'home.html', {'message': 'Some message'})
