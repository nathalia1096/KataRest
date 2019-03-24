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