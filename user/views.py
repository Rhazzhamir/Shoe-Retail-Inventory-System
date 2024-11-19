from django.shortcuts import render

# from user.models import Product , Category


# Create your views here.

def dashboard(request):
    return render(request , "user_dashboard.html")

def change_profile(request):
    return render(request , 'change_profile.html')

def shopping_cart(request):
    return render(request , 'shopping_cart.html')