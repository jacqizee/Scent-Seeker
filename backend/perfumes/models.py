from django.db import models

# Create your models here.
class Perfume(models.Model):
    name = models.CharField(max_length = 50)
    type = models.ForeignKey('perfume_categories.Perfume_Category', on_delete=models.RESTRICT)
    accord = models.ForeignKey('accords.Accord', related_name='perfumes', on_delete=models.RESTRICT)
    gender = models.ForeignKey('genders.Gender', on_delete=models.RESTRICT)
    brand = models.ForeignKey('brands.Brand', on_delete=models.RESTRICT)
    description = models.TextField(max_length = 2000)
    released = models.DateField(blank=True)
    image = models.URLField(max_length=2000)
    top_notes = models.ManyToManyField('notes.Note', related_name="perfumes_top")
    mid_notes = models.ManyToManyField('notes.Note', related_name="perfumes_mid")
    base_notes = models.ManyToManyField('notes.Note', related_name="perfumes_base")
    
    def __str__(self) -> str:
        return f'{self.brand} - {self.name} - {self.type}'