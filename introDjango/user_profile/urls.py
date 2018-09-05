from django.urls import re_path

from user_profile.views import get_profile
urlpatterns = [
    re_path(r'^$', get_profile),
    re_path(r'^(?P<profile_id>\d+)/', get_profile),
]
