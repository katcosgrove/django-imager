from django.test import TestCase
from .models import ImagerProfile, User
import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests"""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


# class ProfileFactory(factory.django.DjangoModelFactory):
#     """Create instances of profiles"""
#     class Meta:
#         model = ImagerProfile

    # bio = factory.Faker('text')
    # phone = factory.Faker('phone_number')
    # location = factory.Faker('city')
    # website = factory.Faker('url')
    # fee = factory.Faker('random_digit')
    # camera = factory.Faker('random_element', elements=[('DSLR', 'Digital Single Lens Reflex'),
    #                        ('M', 'Mirrorless'),
    #                        ('AC', 'Advanced Compact'),
    #                        ('SLR', 'Single Lens Reflex')])

    # services = factory.Faker('random_element', elements=[('weddings', 'Weddings'),
    #                          ('headshots', 'HeadShots'),
    #                          ('landscape', 'LandScape'),
    #                          ('portraits', 'Portraits'),
    #                          ('art', 'Art')])

    # photostyles = factory.Faker('random_element', elements=[('blackandwhite', 'Black and White'),
    #                             ('night', 'Night'),
    #                             ('macro', 'Macro'),
    #                             ('3d', '3D'),
    #                             ('artistic', 'Artistic'),
    #                             ('underwater', 'Underwater')])


def populate_profile(user, **kwargs):
    user.profile.bio = kwargs['bio'] if 'bio' in kwargs else factory.Faker('text')
    user.profile.phone = kwargs['phone'] if 'phone' in kwargs else factory.Faker('phone_number')
    user.profile.location = kwargs['location'] if 'location' in kwargs else factory.Faker('city')
    user.profile.website = kwargs['website'] if 'website' in kwargs else factory.Faker('url')
    user.profile.fee = kwargs['fee'] if 'fee' in kwargs else factory.Faker('random_digit')
    user.profile.camera = kwargs['camera'] if 'camera' in kwargs else factory.Faker('random_element',
                            elements=[('DSLR', 'Digital Single Lens Reflex'),
                           ('M', 'Mirrorless'),
                           ('AC', 'Advanced Compact'),
                           ('SLR', 'Single Lens Reflex')])

    user.profile.services = kwargs['services'] if 'services' in kwargs else factory.Faker('random_element',
                             elements=[('weddings', 'Weddings'),
                             ('headshots', 'HeadShots'),
                             ('landscape', 'LandScape'),
                             ('portraits', 'Portraits'),
                             ('art', 'Art')])

    user.profile.photostyles = kwargs['photostyles'] if 'photostyles' in kwargs else factory.Faker('random_element',
                                elements=[('blackandwhite', 'Black and White'),
                                ('night', 'Night'),
                                ('macro', 'Macro'),
                                ('3d', '3D'),
                                ('artistic', 'Artistic'),
                                ('underwater', 'Underwater')])


class ProfileUnitTest(TestCase):
    """Create and test profiles"""
    @classmethod
    def setUpClass(cls):
        """Setup instances of users for testing"""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            profile = ProfileFactory.create(user=user)
            profile.save()

    @classmethod
    def tearDownClass(cls):
        """Destroy users after test has run"""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        """Test to see if first user has a profile"""
        one_user = User.objects.first()
        # import pdb; pdb.set_trace()
        self.assertIsNotNone(one_user.profile)
