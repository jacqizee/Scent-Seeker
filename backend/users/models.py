from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=50)
    avatar = models.URLField(default='image', max_length=2000)