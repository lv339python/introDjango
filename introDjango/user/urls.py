from django.urls import re_path
from user.views import get_user

urlpatterns = [
    re_path('(?P<user_id>\d+)/', get_user),
]