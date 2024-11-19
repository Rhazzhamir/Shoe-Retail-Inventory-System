from django.shortcuts import render
from django.http import HttpResponse

# from user.models import Product , Category


# Create your views here.

def dashboard(request):
    return render(request , "user_dashboard.html")
