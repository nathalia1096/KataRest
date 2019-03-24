from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Image, UserProfile, Portfolio
import json


# Create your tests here.
class GalleryTestCase(TestCase):