import json


from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View

from helpers.validators import profile_data_validator
from user.models import User
from user_profile.models import UserProfile


def get_profile(request, profile_id=None, user_id=None):
    if request.method == "get":
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

# fname = models.CharField(max_length=20)
#     lname = models.CharField(max_length=20)
#     age = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=True,related_name="my_profile")
def create_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        user = User.get_by_id(data['user_id'])
        if user:
            # profile = UserProfile()
            # profile.user = user
            # profile.lname = data['lname'] if 'lname' in data else ""
            # profile.fname = data.get('fname', "")
            # profile.age = data.get('age', 99)
            # profile.save()

            # profile = UserProfile(lname=data.get('lname', ""),
            #                       fname=data.get('fname', ""),
            #                       age=data.get('age', ""),
            #                       user=user)
            # profile.save()

            # profile = UserProfile(**data)
            # profile.save()

            profile = UserProfile.objects.create(**data)

            return JsonResponse(profile.to_dict(), status=201)

        return JsonResponse({"msg": "user no found"}, status=400)


    return JsonResponse({}, status=400)


class ProfileView(View):
    def get(self, request, user_id=None, profile_id=None):

        profile = UserProfile.get_by_id(profile_id)
        if profile:
            return JsonResponse(profile.to_dict())
        return JsonResponse({}, status=400)
    def post(self, request):
        data = json.loads(request.body)
        user = User.get_by_id(data['user_id'])
        if user:
            profile = UserProfile.create(**data)
            if profile:
                return JsonResponse(profile.to_dict(), status=201)
            return HttpResponseBadRequest()
        return JsonResponse({"msg": "user no found"}, status=400)

    def delete(self, request, profile_id):
        if UserProfile.delete_by_id(profile_id):
            return JsonResponse(status=200)
        return HttpResponseBadRequest()
    def put(self, request, profile_id):

        data = json.loads(request.body)
        profile = UserProfile.get_by_id(profile_id)
        if profile_data_validator(data):
            profile.update(**data)
            return JsonResponse(profile.to_dict(), status=200)
        return HttpResponseBadRequest()
