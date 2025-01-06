

from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard_view, name='seller_dashboard'),
    path('profile_view' , views.profile_view , name='profile_view'),
    path('delete_category/<int:category_id>/', views.delete_category_view, name='delete_category'),
]

