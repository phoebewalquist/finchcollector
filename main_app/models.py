from django.db import models
from django.urls import reverse

# Create your models here.
class Finche(models.Model):
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.breed} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finche_id': self.id})


