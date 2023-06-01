from django.db import models

# Create your models here.
class Finche(models.Model):
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.breed} ({self.id})'

