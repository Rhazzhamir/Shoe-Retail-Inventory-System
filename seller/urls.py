

from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard_view, name='seller_dashboard'),
    path('profile_view' , views.profile_view , name='profile_view'),
    path('delete_category/<int:category_id>/', views.delete_category_view, name='delete_category'),
    path('add-product/', views.add_product_view, name='add_product'),
    # path('delete_product/<int:product_id>/', views.delete_product_view, name='delete_product'),
]


