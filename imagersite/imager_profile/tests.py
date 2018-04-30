from django.test import TestCase, Client
from .models import User
from django.urls import reverse_lazy
import factory
from random import choice


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        """Meta class for a user."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


def populate_profile(user, **kwargs):
    """Populate profile with data."""
    user.profile.bio = kwargs['bio'] if 'bio' in kwargs else factory.Faker('text')
    user.profile.phone = kwargs['phone'] if 'phone' in kwargs else factory.Faker('phone_number')
    user.profile.location = kwargs['location'] if 'location' in kwargs else factory.Faker('city')
    user.profile.website = kwargs['website'] if 'website' in kwargs else factory.Faker('url')
    user.profile.fee = kwargs['fee'] if 'fee' in kwargs else factory.Faker('random_digit')
    user.profile.camera = kwargs['camera'] if 'camera' in kwargs else choice(['DSLR', 'M', 'AC', 'SLR',])
    user.profile.services = kwargs['services'] if 'services' in kwargs else choice(
        ['weddings',
         'headshots',
         'landscape',
         'portraits',
         'art', ])
    user.profile.photostyles = kwargs['photostyles'] if 'photostyles' in kwargs else choice(
        ['blackandwhite',
         'night',
         'macro',
         '3d',
         'artistic',
         'underwater'])


class ProfileUnitTest(TestCase):
    """Create and test profiles."""

    @classmethod
    def setUpClass(cls):
        """Set up instances of users for testing."""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            populate_profile(user, fee='1.00', phone='1234567890')
            user.profile.save()

    @classmethod
    def tearDownClass(cls):
        """Destroy users after test has run."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_has_basic_credentials(self):
        """Test if user has username, email, password."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.username)
        self.assertIsNotNone(one_user.email)
        self.assertIsNotNone(one_user.password)

    def test_user_has_a_profile(self):
        """Test to see if user has a profile."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_user_profile_bio(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.bio)

    def test_user_profile_phone(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.phone)
        self.assertEqual(one_user.profile.phone, '1234567890')

    def test_user_profile_location(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.location)

    def test_user_profile_website(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.website)

    def test_user_profile_fee(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.fee)
        self.assertEqual(one_user.profile.fee, 1.00)

    def test_user_profile_camera(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.camera)

    def test_user_profile_services(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.services)

    def test_user_profile_photostyles(self):
        """Test user profile has content."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.photostyles)

    def test_user_profile_is_active(self):
        """Test if user has active setting and is active."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.active)
        self.assertTrue(one_user.profile.is_active)

    def test_user_can_be_deactivated(self):
        """Deactivate user."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile.active)
        self.assertTrue(one_user.profile.is_active)
        one_user.profile.is_active = False
        self.assertFalse(one_user.profile.is_active)

    def test_user_can_be_deleted(self):
        """Delete user."""
        one_user = User.objects.first()
        one_user.delete()
        self.assertTrue(one_user, None)


class TestProfileViews(TestCase):
    """Class to test profile views."""

    @classmethod
    def setUp(self):
        user = User(username='testing',
                    email='testing@testing.com')
        user.save()
        self.user = user
        self.client = Client()

    @classmethod
    def tearDown(self):
        """Teardown class for test users."""
        User.objects.all().delete()
        super(TestCase, self)

    def test_200_status_on_authenticated_request_to_profile(self):
        """Check for 200 status code."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('profile'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_get_profile_page_404_status_code(self):
        """Test profile page view returns 404 status code."""
        self.client.force_login(self.user)
        response = self.client.get('profilo/', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_get_profile_page_templates(self):
        """Test profile page view templates."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('profile'), follow=True)
        self.assertEqual(response.templates[0].name, 'profile/profile.html')
        self.assertEqual(response.templates[1].name, 'base.html')
