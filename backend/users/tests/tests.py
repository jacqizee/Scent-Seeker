from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
User = get_user_model()

class TestUsers(APITestCase):
    def setUp(self) -> None:
        new_user = User.objects.create(username = 'user1', email = 'emails@email.com')
        new_user.set_password('passing')
        new_user.save()

    def test_create_user(self) -> None:
        user = User.objects.create(username = 'user123', password='password', email='user@email.com')
        self.assertEqual(user.email, 'user@email.com')
        self.assertEqual(user.avatar, 'https://thenounproject.com/icon/perfume-80945/')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
    
    def test_login(self) -> None:
        response = self.client.post(reverse('login'), {
            'username': 'user1',
            'password': 'passing',
        })
        self.assertEqual(response.status_code, 202)

    def test_register(self) -> None:
        response = self.client.post(reverse('register'), {
            'username': 'user2',
            'email': 'user2@email.com',
            'password': 'passing2',
            'password_confirmation': 'passing2'
        })
        self.assertEqual(response.status_code, 201)
