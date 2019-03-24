from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Image(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    isPublic = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    idPortfolio = models.ForeignKey(Portfolio, null=True, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=500, null=True)
    professionalProfile = models.TextField()