from django.db import models

# Create your models here.

class Note_Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length = 500)