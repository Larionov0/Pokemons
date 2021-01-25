from django.test import TestCase
from .models import UserProfile, User
from django.urls import reverse


class RegistrationTest(TestCase):
    def test_redirect_unauthorised_user(self):
        response = self.client.get('/pokemons/main/')
        self.assertIn('auth/login', response.url)

    def test_registration(self):
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='sign_up.html')

        username = 'test_user'
        user_data = {
            'username': username,
            'password1': 't1e2s3t4',
            'password2': 't1e2s3t4'
        }
        response = self.client.post(reverse('auth_sys:register'), data=user_data)
        self.assertEqual(response.status_code, 302)

        user = User.objects.all()[0]
        self.assertEqual(user.username, username)
