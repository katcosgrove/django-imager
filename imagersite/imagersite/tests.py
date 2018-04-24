from django.test import Client
from django.test import TestCase


class ClientTests(TestCase):
    def test_client_login_status_code(self):
        c = Client()
        response = c.post('/accounts/login/', {'username': 'testing', 'password': 'passwordparty'})
        self.assertEqual(response.status_code, 200)

    def test_client_logout(self):
        c = Client()
        response = c.post('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
