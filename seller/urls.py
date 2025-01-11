

from django.urls import path
from . import views
app_name = 'seller'

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard_view, name='seller_dashboard'),
    # path('seller_dashboard/orders/', views.orders_view, name='orders'),
    path('profile_view' , views.profile_view , name='profile_view'),
    path('add-product/', views.add_product_view, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product_view, name='edit_product'),  # Add this line
    path('seller/delete_product/<int:product_id>/', views.delete_product_view, name='delete_product'),
    path('delete_category/<int:category_id>/', views.delete_category_view, name='delete_category'),
    # path('delete_product/<int:product_id>/', views.delete_product_view, name='delete_product'),
    path('delete_deleted_category/<int:category_id>/', views.delete_deleted_category_view, name='delete_deleted_category'),
    path('delete_deleted_product/<int:product_id>/', views.delete_deleted_product_view, name='delete_deleted_product'),
    path('delete-feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
]


