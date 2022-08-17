from django.db import models
from notes.models import Note

# Create your models here.
class Perfume(models.Model):
    accord = models.ForeignKey('accords.Accord', on_delete=models.RESTRICT)
    gender = models.ForeignKey('genders.Gender', on_delete=models.RESTRICT)
    brand = models.ForeignKey('brands.Brand', on_delete=models.RESTRICT)
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 2000)
    released = models.DateField(blank=True)
    image = models.URLField(max_length=2000)
    top_notes = models.ManyToManyField('notes.Note')
    mid_notes = models.ManyToManyField('notes.Note')
    base_notes = models.ManyToManyField('notes.Note')