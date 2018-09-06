from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(default='i@i.ua',)
    pasword = models.CharField(max_length=10, default="root")

    def to_dict(self):
        return {
            "email": self.email,
            "pass": self.pasword
        }
    @staticmethod
    def get_by_id(user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            pass


