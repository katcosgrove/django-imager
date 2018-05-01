from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy


class ClientTests(TestCase):
    """Class for existing user unit tests."""

    def test_user_registration_status_code(self):
        """Test successful user registration status code is 200"""
        response = self.client.post(reverse_lazy('registration_register'),
                                    {'username': 'watdude',
                                     'email': 'watdude@wat.up',
                                     'password1': 'helloworld',
                                     'password2': 'helloworld'},
                                    follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_unsuccessful_registration_status_code(self):
        """Test unsuccessful user registration stays at registration form."""
        response = self.client.post(reverse_lazy('registration_register'),
                                    {'username': 'watdude',
                                     'email': 'watdude@wat.up',
                                     'password1': 'helloworld',
                                     'password2': 'hellewworld'},
                                    follow=True)
        self.assertEqual(response.templates[0].name, 'registration/registration_form.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_user_registration_templates(self):
        """Test successful user registration route to registration complete"""
        response = self.client.post(reverse_lazy('registration_register'),
                                    {'username': 'watdude',
                                     'email': 'watdude@wat.up',
                                     'password1': 'helloworld',
                                     'password2': 'helloworld'},
                                    follow=True)
        self.assertEqual(response.templates[0].name, 'registration/registration_complete.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_client_login_200_status_code(self):
        """Test user login gets a 200 status code."""
        c = Client()
        response = c.post('/accounts/login/', {'username': 'testing', 'password': 'passwordparty'})
        self.assertEqual(response.status_code, 200)

    def test_client_login_404_status_code(self):
        """Test user login gets a 200 status code."""
        c = Client()
        response = c.post('/accounts/loginn/', {'username': 'testing', 'password': 'passwordparty'})
        self.assertEqual(response.status_code, 404)

    def test_client_login_templates(self):
        """Test user login templates."""
        c = Client()
        response = c.post('/accounts/login/', {'username': 'testing', 'password': 'passwordparty'})
        self.assertEqual(response.templates[0].name, 'registration/login.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_client_logout_200_status_code(self):
        """Test a client can log out."""
        c = Client()
        response = c.post('/accounts/logout/')
        self.assertEqual(response.status_code, 200)

    def test_client_logout_404_status_code(self):
        """Test a client can log out."""
        c = Client()
        response = c.post('/accounts/loogie/')
        self.assertEqual(response.status_code, 404)

    def test_client_logout_templates(self):
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
        """Test home page view templates used."""
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
        """Test registration page view templates used."""
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
        self.assertEqual(response.templates[0].name, 'registration/activation_complete.html')
        self.assertEqual(response.templates[1].name, 'base.html')

    def test_user_not_logged_in_302_redirected_status_code(self):
        """Test users not logged in redirected to the homepage."""
        c = Client()
        response = c.get(reverse_lazy('library'))
        self.assertEqual(response.status_code, 302)

    def test_user_not_logged_in_redirected_to_home(self):
        """Test users not logged in redirected to the homepage."""
        c = Client()
        response = c.get(reverse_lazy('library'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'home.html')
        self.assertEqual(response.templates[1].name, 'base.html')
