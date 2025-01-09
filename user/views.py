from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from seller.models import Product
from django.http import JsonResponse
from seller.models import Product 
from .models import Cart
from django.contrib import messages

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

@login_required(login_url='accounts:login')
def about(request):
    return render( request, 'about.html')

@login_required(login_url='accounts:login')
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user
    
    # Check if the product is already in the cart for this user
    cart_item, created = Cart.objects.get_or_create(
        product=product,
        customer=customer,
    )
    
    if not created:
        # If the product already exists in the cart, just increment the quantity
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'Item has been added to your cart.')
    

    return redirect('Customer:shopping_cart') 

@login_required(login_url='accounts:login')
def shopping_cart(request):
    # Fetch cart items for the logged-in user
    customer = request.user
    cart_items = Cart.objects.filter(customer=customer)

    total_items = cart_items.count()

    return render(request, 'shopping_cart.html', {
        'cart_items': cart_items ,
        'total_items': total_items,
        })


@login_required(login_url='accounts:login')
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id, customer=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('Customer:shopping_cart')


def cart(request):
    cart_items = Cart.objects.filter(customer=request.user)
    return render(request, 'shopping_cart.html', {'cart_items': cart_items})

