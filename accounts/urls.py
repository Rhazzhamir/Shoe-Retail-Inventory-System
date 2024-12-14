from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/' , views.register_view , name='register'),
    path('login/' , views.login_view , name='login' ),
    path('logout/' , views.logout_view , name='logout'),

    # customer profile
    path('profile/' , views.profile_view , name='profile'),
    path('User-Profile/' , views.user_profile , name='User-Profile'),
    path('change-password/', views.customer_change_password, name='customer_change_password'),

    # Seller profile
    path('Seller-profile/' , views.seller_profile , name='Seller-Profile'),
    path('change-password/', views.seller_change_password, name='seller_change_password'),

]