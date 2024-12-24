from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from user.models import Product , Category


# Create your views here.

@login_required(login_url='accounts:login')
def dashboard(request):
    return render(request , "user_dashboard.html")

@login_required(login_url='accounts:login')
def shopping_cart(request):
    return render(request , 'shopping_cart.html')

