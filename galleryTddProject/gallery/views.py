from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image, Portfolio, UserProfile
import json

# Create your views here.
@csrf_exempt
def get_list_portfolios(request):
    portfolios_list = Portfolio.objects.all()
    return HttpResponse(serializers.serialize("json", portfolios_list))

@csrf_exempt
def users(request, id=None):
    print("LLAMADA---------------------- +"+ request.method)
    if request.method == 'POST':
        json_user = json.loads(request.body)
        user_name = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=user_name, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
        return HttpResponse(serializers.serialize('json', [user_model]))
    if request.method == 'PUT':
        json_user = json.loads(request.body)
        user_id = json_user['user_id']
        user_name = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.get(pk=id)
        user_model.username = user_name
        user_model.password = password
        user_model.email = email
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.save()

        return HttpResponse(serializers.serialize('json', [user_model]))

@csrf_exempt
def portafolio_usuario(request, id):
    image_list = Image.objects.filter(user=id, isPublic=True)
    return HttpResponse(serializers.serialize("json", image_list))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        password = json_user['password']
        user = User.objects.get(username=username, password=password)
        return HttpResponse(serializers.serialize("json", [user]))

@csrf_exempt
def modify_imageStatus(request):
    if request.method == 'PUT':
        json_images = json.loads(request.body)
        images = json_images['images']
        images_list = []
        for image in images:
            image_model = Image.objects.filter(id=image['image_id']).first()
            image_model.isPublic = image['isPublic']
            image_model.save()
            images_list.append(image_model)

    return HttpResponse(serializers.serialize("json", images_list))

def add_image_portfolio(request, id):
    if request.method == 'POST':
        json_image = json.loads(request.body)
        title = json_image['title']
        url = json_image['url']
        description = json_image['description']
        type = json_image['type']
        isPublic = json_image['isPublic']
        portfolio_model = Portfolio.objects.filter(id=id).first()

        image_model = Image.objects.create(title=title, url=url, description=description, type=type,
                               isPublic=isPublic, user=portfolio_model.user, idPortfolio=portfolio_model)

        image_model.save()
        image_list = Image.objects.filter(idPortfolio=portfolio_model.id)

    return HttpResponse(serializers.serialize("json", image_list))

