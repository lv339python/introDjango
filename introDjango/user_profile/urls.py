from django.urls import re_path

from user_profile.views import get_profile, create_profile, ProfileView
urlpatterns = [
    re_path(r'^$', get_profile),
    re_path(r'^create/$', create_profile),
    re_path(r'^(?P<profile_id>\d+)/', get_profile),
    re_path(r'^(?P<profile_id>\d+)/', ProfileView.as_view()),
    ]

