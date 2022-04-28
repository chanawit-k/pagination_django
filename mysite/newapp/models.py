from django.db import models
from django.forms import CharField, FloatField

# Create your models here.
class Movies(models.Model):
    def __str__(self):
        return self.name


    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
