from tabnanny import verbose
from django.db import models

# Create your models here.

class Note_Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Note Category'
        verbose_name_plural = 'Note Categories'