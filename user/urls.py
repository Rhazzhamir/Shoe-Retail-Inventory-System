

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user_dashboard/' , views.dashboard , name='user_dashboard'),
]
