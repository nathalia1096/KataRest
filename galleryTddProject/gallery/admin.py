from django.contrib import admin
from .models import Image, Portfolio, UserProfile

# Register your models here.
admin.site.register(Image)
admin.site.register(Portfolio)
admin.site.register(UserProfile)