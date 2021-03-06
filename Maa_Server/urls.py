"""Maa_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from welcome.views import welcome
from vaccin_schedule.views import vaccin
from maps.views import map_view
from login.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', welcome),
    url(r'^vaccin/', vaccin),
    url(r'^map/', map_view),
    url(r'^login/', login),
    # url(r'fcm/', include('fcm.urls')),
]
