from django.db import models

# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('note_categories.Note_Category', on_delete=models.RESTRICT, default = None)
    image = models.URLField(max_length = 2000, default = None)
    description = models.TextField(max_length = 500, blank = True)

    def __str__(self):
        return f'{self.category} - {self.name}'