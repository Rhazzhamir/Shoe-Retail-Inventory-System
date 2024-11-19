

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('seller_dashboard/', views.dashboard, name='seller_dashboard'),
]
