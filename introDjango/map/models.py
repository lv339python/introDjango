from django.db import models

# Create your models here.

class Map(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=10)
