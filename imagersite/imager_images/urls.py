from django.urls import path
from .views import library_view


urlpatterns = [
    path('', library_view, name='library'),
    # path('<str:username>/', profile_view, name='named_profile'),
    # path('settings/<str:username>', profile_view, name='settings'),  #The view is not correct here
]
