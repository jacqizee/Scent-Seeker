from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=50)
    avatar = models.CharField(default='image')
    gender = models.CharField(blank=True)