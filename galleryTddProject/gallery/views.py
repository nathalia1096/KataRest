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
def users(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        print("JSON->");
        print(json_user)
        user_name = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        print(user_name);
        user_model = User.objects.create_user(username=user_name, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()

        return HttpResponse(serializers.serialize('json', [user_model]))