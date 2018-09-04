from django.db import models

# Create your models here.
from user.models import User


class UserProfile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=True)

