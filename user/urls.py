

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Customer'

urlpatterns = [
    path('user_dashboard/' , views.dashboard , name='user_dashboard'),
    # path('change_profile' , views.change_profile , name='change_profile'),
    path('shopping_cart/' , views.shopping_cart , name='shopping_cart'),
    path('about/' , views.about , name='about'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    path('orders/', views.orders, name='orders'), 
]
