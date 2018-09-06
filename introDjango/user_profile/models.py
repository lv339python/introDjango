from django.db import models

# Create your models here.
from user.models import User


class UserProfile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=True,related_name="my_profile")

    def to_dict(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'age': self.age
        }

    @staticmethod
    def get_by_id(profile_id):
        try:
            return UserProfile.objects.get(pk=profile_id)
        except:
            pass
    @staticmethod
    def get_by_user_id(user_id):
        try:
            return UserProfile.objects.get(user=user_id)
        except:
            pass
