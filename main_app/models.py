from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    anime = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} ({self.id})'