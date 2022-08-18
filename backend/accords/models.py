from django.db import models

# Create your models here.
class Accord(models.Model):
    name = models.CharField(max_length = 30, unique=True)

    def __str__(self) -> str:
        return self.name