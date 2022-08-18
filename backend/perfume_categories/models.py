from django.db import models

# Create your models here.
class Perfume_Category(models.Model):
    type = models.CharField(max_length = 30, unique=True)