from django.urls import re_path, include
from user.views import get_user

urlpatterns = [
    re_path(r'^$', get_user),
    re_path(r'^(?P<user_id>\d+)/$', get_user),
    re_path(r'^(?P<user_id>\d+)/profile/', include('user_profile.urls')),
]
