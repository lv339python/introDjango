"""introDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.get_home),
    path('user/', include('user.urls')),
    path('profile/', include('user_profile.urls'))
]

# from info.views import info, info_boo
# from map.views import get_dict
#
# urlpatterns = [
#     path('info/', info),
#     path('info/boo', info_boo),
#     path('map/dict', get_dict)
# ]
