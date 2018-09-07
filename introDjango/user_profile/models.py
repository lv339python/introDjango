from django.db import models

# Create your models here.
from user.models import User


class UserProfile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=True, related_name="my_profile")

    def to_dict(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'age': self.age
        }

    @staticmethod
    def create(fname, lname, age, user):
        profile = UserProfile()
        profile.user = user
        profile.lname = lname
        profile.fname = fname
        profile.age = age
        try:
            profile.save()
        except:
            return None
        return profile

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
    @staticmethod
    def delete_by_id(profile_id):
        profile = UserProfile.get_by_id(profile_id)
        try:
            profile.delete()
        except:
            return None
        return True

    def update(self, fname=None, lname=None, age=None):
        if fname:
            self.fname = fname
        if lname:
            self.lname = lname
        if age is None:
            self.age = age
        self.save()
