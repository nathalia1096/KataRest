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