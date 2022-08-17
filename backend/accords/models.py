from django.db import models

# Create your models here.
class Accord(models.model):
    name = models.CharField(max_length = 30)