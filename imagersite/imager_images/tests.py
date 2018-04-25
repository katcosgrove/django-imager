from django.test import TestCase
from .models import User, Album, Photo
import factory

# Create your tests here.
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ImageFactory(factor)