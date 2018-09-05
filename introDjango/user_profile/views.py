from django.http import JsonResponse

from user.models import User
from user_profile.models import UserProfile


def get_profile(request, profile_id=None, user_id=None):
    print(user_id, profile_id)
    if user_id:
        user = User.get_by_id(user_id)
        data = {}
        profile = user.my_profile.first()
        data.update(user.to_dict())
        data[profile.id] = profile.to_dict()
        # profile = UserProfile.get_by_user_id(user_id)
        # data.update(profile.to_dict())
        return JsonResponse(data, status=200)
    if profile_id:
        profile = UserProfile.get_by_id(profile_id)
        data = profile.to_dict()
        data[profile.user.id] = profile.user.to_dict()
        if profile:
            return JsonResponse(data, status=200)
    return JsonResponse({}, status=400)
