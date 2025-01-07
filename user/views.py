from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from seller.models import Product

# Create your views here.

@login_required(login_url='accounts:login')
def dashboard(request):
    products = Product.objects.all()  # Fetch all products
    context = {
        'products': products,
    }
    return render(request , "user_dashboard.html" , context)

@login_required(login_url='accounts:login')
def shopping_cart(request):
    return render(request , 'shopping_cart.html')

def about(request):
    return render( request, 'about.html')
