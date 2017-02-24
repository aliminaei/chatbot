from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^fb_messages$', views.fb_messages, name='fb_messages'),
]
