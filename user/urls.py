

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Customer'

urlpatterns = [
    path('user_dashboard/' , views.dashboard , name='user_dashboard'),
    # path('change_profile' , views.change_profile , name='change_profile'),
    path('shopping_cart/' , views.shopping_cart , name='shopping_cart'),
    path('about/' , views.about , name='about'),
]
