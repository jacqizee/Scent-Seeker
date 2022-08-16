from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=50)
    avatar = models.URLField(default='https://thenounproject.com/icon/perfume-80945/', max_length=2000)