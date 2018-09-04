from django.http import JsonResponse
from .models import User

def get_user(request, user_id=None):
    print(user_id)
    if user_id:
        try:
            user = User.objects.get(pk=int(user_id))
        except:
            user = User()
        return JsonResponse(user.to_dict())

    users = User.objects.all()
    print(type(users))
    users = [user.to_dict() for user in users]
    return JsonResponse()

