from django.http import JsonResponse
from .models import User

def get_user(request, user_id=None):
    print(user_id)
    if user_id:
        user = User.get_by_id(user_id)
        if user:
            return JsonResponse(user.to_dict(), status=200)
        return JsonResponse({}, status=400)
    # user2 = User(email="sss", pasword="dsfdsgfs")
    # user2.save()
    users = User.objects.all()[:30]
    print(type(users))
    users = [user.to_dict() for user in users]
    return JsonResponse(users, safe=False)

