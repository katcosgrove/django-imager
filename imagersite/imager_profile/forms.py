from .models import ImagerProfile
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, widgets


class ProfileEditForm(ModelForm):
    """Class for profile edit form."""

    email = CharField(
        max_length=User._meta.get_field('email').max_length,
        widget=widgets.EmailInput())
    first_name = CharField(
        max_length=User._meta.get_field('first_name').max_length,
        required=False)
    last_name = CharField(
        max_length=User._meta.get_field('last_name').max_length,
        required=False)

    class Meta:
        """Meta info for update form."""

        model = ImagerProfile
        fields = ['first_name', 'last_name', 'bio', 'phone', 'location', 'website', 'fee']

    def __init__(self, *args, **kwargs):
        """Initialize form data."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = User.objects.get(username=username)
        self.fields['first_name'].initial = User.objects.get(username=username)
        self.fields['last_name'].initial = User.objects.get(username=username)
