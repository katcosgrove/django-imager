from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy


class ClientTests(TestCase):
    """Class for existing user unit tests."""

    def test_user_registration(self):
        """Test for user registration."""
        response = self.client.post(reverse_lazy('registration_register'), 
            {'username': 'watdude',  
            'email': 'watdude@wat.up', 
            'password1': 'helloworld', 
            'password2': 'helloworld'}, 
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/registration_complete.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_client_login_status_code(self):
        """Test user login gets a 200 status code."""
        c = Client()
        response = c.post('/accounts/login/', {'username': 'testing', 'password': 'passwordparty'})
        self.assertEqual(response.status_code, 200)

    def test_client_logout_status_code(self):
        """Test a client can log out."""
        c = Client()
        response = c.post('/accounts/logout/')
        self.assertEqual(response.status_code, 200)

    def test_client_logout_status_code(self):
        """Test a client can log out."""
        c = Client()
        response = c.post('/accounts/logout/')
        self.assertEqual(response.templates[0].name, 'registration/logout.html')
        self.assertEqual(response.templates[1].name, 'base.html')


class ViewTests(TestCase):
    """Class for unit testing views."""
    def test_get_home_page_status_codes(self):
        """Test home page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_get_home_page_templates(self):
        """Test home page view templates used"""
        c = Client()
        response = c.get(reverse_lazy('home'))
        self.assertEqual(response.templates[0].name, 'home.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_get_registration_page_status_codes(self):
        """Test registration page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_get_registration_page_templates(self):
        """Test registration page view templates used"""
        c = Client()
        response = c.get(reverse_lazy('registration_register'))
        self.assertEqual(response.templates[0].name, 'registration/registration_form.html')
        self.assertEqual(response.templates[1].name, 'base.html') 

    def test_get_login_page_status_code(self):
        """Test login page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('auth_login'))
        self.assertEqual(response.status_code, 200)

    def test_get_login_page_templates(self):
        """Test login page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('auth_login'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/login.html')
        self.assertEqual(response.templates[1].name, 'base.html') 

    def test_get_logout_page_status_code(self):
        """Test logout page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('auth_logout'))
        self.assertEqual(response.status_code, 200)

    def test_get_logout_page_templates(self):
        """Test logout page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('auth_logout'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/logout.html')
        self.assertEqual(response.templates[1].name, 'base.html') 

    def test_get_registration_complete_page_status_code(self):
        """Test registration complete page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('registration_complete'))
        self.assertEqual(response.status_code, 200)

    def test_get_registration_complete_page_templates(self):
        """Test registration complete page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('registration_complete'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/registration_complete.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_get_activation_complete_page_status_code(self):
        """Test activation complete page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('registration_activation_complete'))
        self.assertEqual(response.status_code, 200)

    def test_get_activation_complete_page_templates(self):
        """Test activation complete page view returns 200 status code."""
        c = Client()
        response = c.get(reverse_lazy('registration_activation_complete'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'registration/activation_complete.html')
        self.assertEqual(response.templates[1].name, 'base.html')



