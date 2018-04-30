from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy
from .models import Album, Photo
from imager_profile.models import User
import factory
import faker


fake = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        """Meta class for a user."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create instances of Photos."""

    class Meta:
        """Meta class for a photo."""

        model = Photo

    image = SimpleUploadedFile('test.jpg', b'file_content', content_type='image/jpg')
    title = factory.Faker('word')
    description = factory.Faker('text')
    date_uploaded = factory.Faker('date')
    date_modified = factory.Faker('date')
    date_published = factory.Faker('date')
    published = factory.Faker('random_element', elements=[
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ])


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create instances of Albums."""

    class Meta:
        """Meta class for an album."""

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
    ])


class PhotoAlbumUnitTest(TestCase):
    """Test Album functionality and interactivity."""

    @classmethod
    def setUpUser(self):
        """Create a single album instance."""
        super(TestCase, self)
        user = User.build(username='watdude',
                          email='watdude@wat.up')
        user.set_password('helloworld')
        user.user_id = 1
        user.save()
        self.user = user

    @classmethod
    def setUpAlbum(self):
        """Create a single album instance."""
        super(TestCase, self)
        album = AlbumFactory.build()
        album.user = self.user
        album.save()
        self.album = album

    @classmethod
    def setUpPhoto(self):
        """Create a single photo instance."""
        super(TestCase, self)
        photo = PhotoFactory.build()
        photo.user = self.user
        photo.save()
        self.photo = photo

    @classmethod
    def tearDownPhotoAlbums(self):
        """Destroy photo album instance."""
        super(TestCase, self)
        Album.objects.all().delete()
        User.objects.all().delete()
        Photo.objects.all().delete()

    def test_album_is_being_created(self):
        """Test if an album is created."""
        one_album = Album
        self.assertIsNotNone(one_album)

    def test_album_has_a_user(self):
        """Test if album has a user."""
        one_album = Album
        one_album.user = User
        self.assertIsNotNone(one_album.user)
        self.assertEqual(one_album.user, User)

    def test_album_has_a_title(self):
        """Test if an album has a title."""
        one_album = Album
        self.assertTrue(one_album.title)

    def test_album_has_a_description(self):
        """Test if an album has a description."""
        one_album = Album
        self.assertTrue(one_album.description)

    def test_photo_is_being_created(self):
        """Test if a photo is created."""
        one_photo = Photo
        self.assertIsNotNone(one_photo)

    def test_photo_has_a_user(self):
        """Test photo belongs to a user."""
        one_photo = Photo
        one_photo.user = User
        self.assertIsNotNone(one_photo.user)
        self.assertEqual(one_photo.user, User)

    def test_photo_has_an_image(self):
        """Test if a photo has an image."""
        one_photo = Photo
        self.assertIsNotNone(one_photo.image)

    def test_photo_has_a_title(self):
        """Test if a photo has a title."""
        one_photo = Photo
        self.assertIsNotNone(one_photo.title)

    def test_photo_added_to_album(self):
        """Test a photo is successfully added to an album."""
        one_photo = Photo
        one_album = Album
        one_photo.album = one_album
        self.assertTrue(one_photo.album, one_album)
        self.assertTrue(one_album.__sizeof__, 1)

    def test_multiple_photos_added_to_album(self):
        """Test a multiple photos can be added to a single album."""
        one_photo = Photo
        two_photo = Photo
        three_photo = Photo
        one_album = Album
        one_photo.album = one_album
        two_photo.album = one_album
        three_photo.album = one_album
        self.assertTrue(one_photo.album, one_album)
        self.assertTrue(two_photo.album, one_album)
        self.assertTrue(three_photo.album, one_album)
        self.assertTrue(one_album.__sizeof__, 3)

    def test_one_photo_added_to_multiple_albums(self):
        """Test the same photos can be added to multiple albums."""
        one_album = Album
        two_album = Album
        three_album = Album
        one_photo = Photo
        one_album.photo = one_photo
        two_album.photo = one_photo
        three_album.photo = one_photo
        self.assertIs(one_photo, one_album.photo)
        self.assertIs(one_album.photo, three_album.photo)
        self.assertIs(three_album.photo, two_album.photo)


class TestImagesViews(TestCase):
    """Class to test image views."""

    @classmethod
    def setUp(self):
        user = User(username='testing',
                    email='testing@testing.com')
        user.save()
        self.user = user
        self.client = Client()

        photo = PhotoFactory.build()
        photo.user_id = self.user.id
        photo.save()
        self.photo = photo

        album = AlbumFactory.build()
        album.user_id = self.user.id
        album.save()
        self.album = album

    @classmethod
    def tearDown(self):
        """Teardown class for test users."""
        User.objects.all().delete()
        super(TestCase, self)

    def test_200_status_on_authenticated_request_to_library(self):
        """Check for 200 status code."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_get_library_page_404_status_code(self):
        """Test library page view returns 404 status code."""
        self.client.force_login(self.user)
        response = self.client.get('images/libary/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_get_library_page_templates(self):
        """Test library page view templates."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('library'), follow=True)
        self.assertEqual(response.templates[0].name, 'images/library.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_200_status_on_authenticated_request_to_albums(self):
        """Check for 200 status code."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('albums'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_get_albums_page_404_status_code(self):
        """Test library page view returns 404 status code."""
        self.client.force_login(self.user)
        response = self.client.get('images/alum', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_get_album_page_templates(self):
        """Test library page view templates."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('albums'), follow=True)
        self.assertEqual(response.templates[0].name, 'images/albums.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_200_status_on_authenticated_request_to_photos(self):
        """Check for 200 status code."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('photos'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_get_photos_page_404_status_code(self):
        """Test library page view returns 404 status code."""
        self.client.force_login(self.user)
        response = self.client.get('images/photogs/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_get_photos_page_templates(self):
        """Test library page view templates."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('photos'), follow=True)
        self.assertEqual(response.templates[0].name, 'images/photos.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_200_status_on_authenticated_request_to_image(self):
        """Test 200 status code on authenticated request to single image."""
        self.client.force_login(self.user)
        response = self.client.get('/images/photos/{}'.format(self.photo.id))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_302_status_on_unauthenticated_request_to_image(self):
        """Test 200 status code on unauthenticated request to single image."""
        response = self.client.get('/images/photos/{}'.format(self.photo.id))
        self.assertEqual(response.status_code, 200)

    def test_404_status_on_bad_request_to_product(self):
        """Test bad photo page view returns 404 status code."""
        response = self.client.get('/images/photos/does_not_exist')
        self.assertEqual(response.status_code, 404)

    def test_200_status_on_authenticated_request_to_album(self):
        """Test 200 status code on authenticated request to single image."""
        self.client.force_login(self.user)
        response = self.client.get('/images/albums/{}'.format(self.album.id))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_302_status_on_unauthenticated_request_to_album(self):
        """Test 200 status code on unauthenticated request to single image."""
        response = self.client.get('/images/albums/{}'.format(self.album.id))
        self.assertEqual(response.status_code, 302)

    def test_404_status_on_bad_request_to_album(self):
        """Test bad photo page view returns 404 status code."""
        response = self.client.get('/images/albums/does_not_exist')
        self.assertEqual(response.status_code, 404)
