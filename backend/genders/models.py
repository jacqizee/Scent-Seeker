from django.db import models

# Create your models here.
class Gender(models.model):
    GENDER_CHOICES = ['Feminine', 'Masculine', 'Unisex']
    type = models.CharField(choices=GENDER_CHOICES)