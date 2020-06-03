 
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class TestPosts(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            # self.user = User.objects.create_user(
            username = "fake",
            email = "fake@trial.com",
            password = 'wordpass'
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/users/profile/1/')

    def test_create_view(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 302)

    def test_create_view_template(self):
        response = self.client.get(reverse('create_post'))
        self.assertTemplateUsed('post_create.html')