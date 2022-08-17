from django.db import models

# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('note_categories.Category', on_delete=models.RESTRICT)
    image = models.URLField(max_length = 2000)
    description = models.TextField(max_length = 500, blank=True)