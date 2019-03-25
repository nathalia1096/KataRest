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