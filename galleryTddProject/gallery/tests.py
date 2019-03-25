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
        user_model2 = User.objects.create_user(username='test2', password='kd8wke-DE34', first_name='test2',
                                              last_name='test2',
                                              email='test2@test.com')
        Portfolio.objects.create(user=user_model)
        Portfolio.objects.create(user=user_model2)

        response = self.client.get('/gallery/getPortfolios/')
        current_data = json.loads(response.content)

        self.assertEqual(len(current_data), 2)




    def test_registrar_usuario(self):
        url = '/gallery/users/'
        response = self.client.get(url, json.dumps(
            {"user": "test", "first_name": "testx", "last_name": "xxtest", "password": "testxxx",
             "email": "test@test.com", "professionalProfile": "xxtest", "photo": "Test1"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        currentData = json.loads(response.content)
        self.assertEqual(currentData[0]['fields']['username'], "utest")
