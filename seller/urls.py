

from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard_view, name='seller_dashboard'),
    path('profile_view' , views.profile_view , name='profile_view'),
    path('add-product/', views.add_product_view, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product_view, name='edit_product'),  # Add this line
    path('seller/delete_product/<int:product_id>/', views.delete_product_view, name='delete_product'),
    path('delete_category/<int:category_id>/', views.delete_category_view, name='delete_category'),
    # path('delete_product/<int:product_id>/', views.delete_product_view, name='delete_product'),
    path('delete_deleted_category/<int:category_id>/', views.delete_deleted_category_view, name='delete_deleted_category'),
    path('delete_deleted_product/<int:product_id>/', views.delete_deleted_product_view, name='delete_deleted_product'),
    
]


