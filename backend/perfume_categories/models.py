from django.db import models

# Create your models here.
class Perfume_Category(models.Model):
    type = models.CharField(max_length = 30, unique=True)

    class Meta:
        verbose_name = 'Perfume Category'
        verbose_name_plural = 'Perfume Categories'

    def __str__(self) -> str:
        return self.type