from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.test import TestCase


class User_test(TestCase):
    # method which is called before the tests start
    def setUp(self):
        self.user_1 = User.objects.create_user("user1", "email@gmail.com", "password")
        pass

    # method which is called after the tests finished
    def tearDown(self):
        self.user_1.delete()
        pass

    # testing working of the username
    def test_username(self):
        self.assertEquals(self.user_1.get_username(), 'user1')

    # testing working of the email
    def test_email(self):
        self.assertEquals(self.user_1.email, 'email@gmail.com')

    # testing working of the password
    def test_password(self):
        self.assertTrue(self.user_1.check_password('password'))

    # testing working of the sign_in method
    def test_signIn(self):
        self.assertTrue(authenticate(username="user1", password="password"))
