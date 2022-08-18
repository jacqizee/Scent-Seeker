from django.db import models

# Create your models here.
class Gender(models.Model):
    type = models.CharField(max_length = 15)

    def __str__(self) -> str:
        return self.type