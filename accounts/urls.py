# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/' , views.register_view , name='register'),
    path('login/' , views.login_view , name='login' ),
    path('logout/' , views.logout_view , name='logout'),

    # profile
    path('profile/' , views.profile_view , name='profile'),
    path('User-Profile/' , views.user_profile , name='User-Profile'),
    path('change-password/', views.change_password, name='change_password'),

]