from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('', views.home, name='home'),
    path('signout', views.signout, name='signout'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('scan', views.scan, name='scan')
]
