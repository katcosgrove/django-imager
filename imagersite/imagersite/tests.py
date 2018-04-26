from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy


class ClientTests(TestCase):
    """Class for existing user unit tests."""
    def test_client_login_status_code(self):
        """Test user login gets a 200 status code."""
        c = Client()
        response = c.post('/accounts/login/', {'username': 'testing', 'password': 'passwordparty'})
        self.assertEqual(response.status_code, 200)

    def test_client_logout(self):
        """Test a client can log out."""
        c = Client()
        response = c.post('/accounts/logout/')
        self.assertEqual(response.status_code, 200)


class ViewTests(TestCase):
    """Class for unit testing views."""
    def test_get_home_page(self):
        """Test home page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_get_registration_page(self):
        """Test registration page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_get_login_page(self):
        """Test login page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('auth_login'))
        self.assertEqual(response.status_code, 200)
