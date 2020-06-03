from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            # self.user = User.objects.create_user(
            username = "fake",
            email = "fake@trial.com",
            password = 'wordpass'
        )


    def test_user_aunthentication(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/users/profile/1/')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


    def test_login_page_template(self):
        response = self.client.post(reverse('login'))
        self.assertTemplateUsed('login.html')

    def test_signup_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed('register.html')

    def test_str_representation(self):
        self.assertEqual(str(self.user), 'fake' )