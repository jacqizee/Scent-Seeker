from django.contrib.auth import get_user_model
from django.test import TestCase

class TestUsers(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(username = 'user123', password='password', email='user@email.com')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)