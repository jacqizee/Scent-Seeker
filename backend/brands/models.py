from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length = 50)
    logo = models.URLField(max_length = 2000)
    description = models.TextField(max_length = 1000)

    def __str__(self) -> str:
        return self.name