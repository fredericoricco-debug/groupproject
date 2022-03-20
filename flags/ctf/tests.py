from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.test import TestCase


class User_test(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user("user1", "email@gmail.com", "password")
        pass

    def tearDown(self):
        self.user_1.delete()
        pass

    def test_username(self):
        self.assertEquals(self.user_1.get_username(), 'user1')

    def test_email(self):
        self.assertEquals(self.user_1.email, 'email@gmail.com')

    def test_password(self):
        self.assertTrue(self.user_1.check_password('password'))

    def test_signIn(self):
        self.assertTrue(authenticate(username="user1", password="password"))
