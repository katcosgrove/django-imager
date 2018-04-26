from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Album, Photo
from imager_profile.models import User, ImagerProfile
import factory
import faker


fake = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """creates a test user for writing tests"""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create instances of Photos"""
    class Meta:
        model = Photo

    image = SimpleUploadedFile('test.jpg', b'file_content', content_type='image/jpg')
    title = factory.Faker('text') 
    description = factory.Faker('text') 
    date_uploaded = factory.Faker('date') 
    date_modified = factory.Faker('date') 
    date_published = factory.Faker('date') 
    published = factory.Faker('random_element', elements=[
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
        ]
    )


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create instances of Albums"""
    class Meta:
        model = Album

    title = fake.text(170)
    description = factory.Faker('text') 
    date_uploaded = factory.Faker('date') 
    date_modified = factory.Faker('date') 
    date_published = factory.Faker('date') 
    published = factory.Faker('random_element', elements=[
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
        ]
    )


class AlbumUnitTest(TestCase):
    """Test Album functionality and interactivity"""

    def setUpAlbums(self):
        """Create a single album instance"""
        user = UserFactory.create()
        user.set_password(factory.Faker('password'))
        user.user_id = 1
        user.save()
        self.user = user

        album = AlbumFactory.build()
        album.user = self.user
        album.save()
        self.album = album

    def test_album_is_being_created(self):
        """Test if an album is created"""
        one_album = Album
        self.assertIsNotNone(one_album)

    def test_album_has_things(self):
        """Test if an album has a title"""
        one_album = Album
        self.assertTrue(one_album.title)

    def test_album_has_things(self):
        """Test if an album has a description"""
        one_album = Album
        self.assertTrue(one_album.description)


class PhotoUnitTest(TestCase):
    """Test Photo functionality and interactivity"""
    
    @classmethod
    def setUpPhotos(cls):
        """Create a single photo instance"""
        super(TestCase, cls)
        photo = PhotoFactory.create()
        photo.save()

    @classmethod
    def tearDownphotos(cls):
        """Destroy single photo instance"""
        super(TestCase, cls)
        Photo.objects.all().delete()

    def test_photo_is_being_created(self):
        """Test if an photo is created"""
        one_photo = Photo
        self.assertIsNotNone(one_photo)

    def test_photo_has_an_image(self):
        """Test if an photo has an image"""
        one_photo = Photo
        self.assertIsNotNone(one_photo.image)

    def test_photo_has_a_title(self):
        """Test if an photo has a title"""
        one_photo = Photo
        self.assertIsNotNone(one_photo.title)