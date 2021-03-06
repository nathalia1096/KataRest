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
        response = self.client.post(url, json.dumps(
            {"username": "test", "first_name": "testx", "last_name": "xxtest", "password": "testxxx",
             "email": "test@test.com", "professionalProfile": "xxtest", "photo": "Test1"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        currentData = json.loads(response.content)
        self.assertEqual(currentData[0]['fields']['username'], "test")

    def test_ver_portafolio_publico(self):
        user = User.objects.create_user(username='user', password='1234ABC', first_name='test',
                                        last_name='test', email='test@uniandes.edu.co')
        Image.objects.create(title='Test1', url='No', description='Test', type='jpg',
                             user=user, isPublic=True)
        Image.objects.create(title='Test2', url='No', description='Test2', type='jpg',
                             user=user, isPublic=False)
        url = '/gallery/users/' + str(user.id) + '/portafolio'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 1)
        self.assertEqual(current_data[0]['fields']['title'], 'Test1')

    def test_login(self):
        user = User.objects.create_user(username='user123', password='1234ABC', first_name='test',
                                        last_name='test', email='test@uniandes.edu.co')
        response = self.client.post('/gallery/login/', json.dumps(

            {"username":user.username, "password":user.password}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(current_data[0]['fields']['username'], 'user123')

    def test_edicion_usuario(self):
        user = User.objects.create_user(username='user123', password='1234ABC', first_name='test',
                                        last_name='test', email='test@uniandes.edu.co')
        url = '/gallery/users/' + str(user.id)

        response = self.client.put(url, json.dumps({"user_id": user.id, "username": "test", "first_name": "testx",
                                                    "last_name": "xxtest", "password": "testxxx",
                                                    "email": "test@test.com"}), content_type='application/json')

        current_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(current_data[0]['fields']['username'], 'test')

    def test_verify_imageStatus(self):
        user_model = User.objects.create_user(username='user123', password='1234ABC', first_name='test',
                                        last_name='test', email='test@uniandes.edu.co')

        portfolio_model = Portfolio.objects.create(user=user_model)

        image1_model = Image.objects.create(title="Image1", url="Image1.jpg", description="Description1", type="jpg",
                                isPublic=True, user=user_model, idPortfolio=portfolio_model)

        image2_model = Image.objects.create(title="Image2", url="Image2.jpg", description="Description2", type="jpg",
                             isPublic=True, user=user_model, idPortfolio=portfolio_model)

        response = self.client.put('/gallery/modifyImageStatus/', json.dumps(
            {"images": [{"image_id": image1_model.id, "isPublic": False}, {"image_id": image2_model.id, "isPublic": False}]}), content_type='application/json')

        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['isPublic'], False)
        self.assertEqual(current_data[1]['fields']['isPublic'], False)

    def test_add_image_portfolio(self):
        user_model = User.objects.create_user(username='user123', password='1234ABC', first_name='test',
                                              last_name='test', email='test@uniandes.edu.co')

        portfolio_model = Portfolio.objects.create(user=user_model)

        Image.objects.create(title="Image1", url="Image1.jpg", description="Description1", type="jpg",
                                            isPublic=True, user=user_model, idPortfolio=portfolio_model)

        Image.objects.create(title="Image2", url="Image2.jpg", description="Description2", type="jpg",
                                            isPublic=True, user=user_model, idPortfolio=portfolio_model)

        response = self.client.post('/gallery/addImage/' + str(portfolio_model.id) + '/', json.dumps(
            {"title": 'Image3', "url": 'Image3.jpg', "description": 'Description3', "type": 'jpg',
             "isPublic": True}), content_type='application/json')

        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 3)
        self.assertEqual(current_data[0]['fields']['title'], "Image3")

