from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Image, UserProfile, Portfolio
import json


# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_portfolios_status(self):
        url = '/gallery/getPortfolios/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_portfolios_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test',
                                              email='test@test.com')
        Portfolio.objects.create(user=user_model)
        Portfolio.objects.create(user=user_model)

        response = self.client.get('/gallery/getPortfolios/')
        current_data = json.loads(response.content)

        self.assertEqual(len(current_data), 2)