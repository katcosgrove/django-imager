from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<str:username>/', ProfileView.as_view(), name='named_profile'),
    path('settings/<str:username>', ProfileView.as_view(), name='settings'),  # The view is not correct here
]
