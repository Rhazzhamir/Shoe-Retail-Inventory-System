from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from seller.models import Product
from django.http import JsonResponse
from seller.models import Product 
from .models import Cart , Order ,Feedback
from django.contrib import messages
from decimal import Decimal
from django.db import transaction
from django.http import HttpResponse
import json
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


def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'components/user_orders.html', {'orders': user_orders})

@login_required(login_url='accounts:login')
# def checkout(request):
#     if request.method == 'POST':
#         selected_items = request.POST.getlist('selected_items')
#         for item_id in selected_items:
#             cart_item = Cart.objects.get(id=item_id)
#             Order.objects.create(
#                 user=request.user,
#                 product=cart_item.product,
#                 quantity=cart_item.quantity,
#                 total_price=cart_item.product.price * cart_item.quantity
#             )
#             cart_item.delete()  
#         return redirect('Customer:orders')  
#     return redirect('Customer:shopping_cart')

def checkout(request):
    if request.method == 'POST':
        try:
            selected_items = request.POST.getlist('selected_items[]')
            
            if not selected_items:
                messages.error(request, "Please select items to checkout!")
                return redirect('Customer:cart')

            with transaction.atomic():
                cart_items = Cart.objects.filter(
                    customer=request.user,
                    id__in=selected_items
                ).select_related('product')
                
                # Check if any selected product has zero stock
                for cart_item in cart_items:
                    if cart_item.product.stock == 0:
                        messages.error(request, f"{cart_item.product.product_name} is out of stock!")
                        return redirect('Customer:cart')
                
                # Process checkout for items with stock
                for cart_item in cart_items:
                    total_price = Decimal(cart_item.product.price) * cart_item.quantity
                    
                    # Create order
                    Order.objects.create(
                        user=request.user,
                        product=cart_item.product,
                        quantity=cart_item.quantity,
                        total_price=total_price
                    )
                    
                    # Update stock
                    cart_item.product.stock -= cart_item.quantity
                    cart_item.product.save()
                    
                    # Remove from cart
                    cart_item.delete()
                
                messages.success(request, "Order placed successfully!")
                return redirect('Customer:orders')
                
        except Exception as e:
            messages.error(request, "An error occurred during checkout.")
            return redirect('Customer:cart')
            
    return redirect('Customer:cart')

def cancel_order(request, order_id):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Get the order and ensure it belongs to the current user
                order = get_object_or_404(Order, id=order_id, user=request.user)
                
                # Increase the product stock
                product = order.product
                product.stock += order.quantity
                product.save()
                
                # Delete the order
                order.delete()
                
                messages.success(request, "Order has been successfully cancelled and stock has been restored.")
                
        except Exception as e:
            messages.error(request, "An error occurred while cancelling the order.")
            
    return redirect('Customer:orders')

def submit_feedback(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id, user=request.user)
        feedback_text = request.POST.get('feedback_text')
        
        if feedback_text:
            Feedback.objects.create(
                user=request.user,
                order=order,
                feedback_text=feedback_text
            )
            messages.success(request, 'Thank you for your feedback!')
        else:
            messages.error(request, 'Please provide feedback text.')
            
    return redirect('Customer:user_orders')

def delete_feedback(request, feedback_id):
    if request.method == 'POST':
        feedback = get_object_or_404(Feedback, id=feedback_id)
        if request.user == feedback.user or request.user.is_staff:
            feedback.delete()
            messages.success(request, 'Feedback deleted successfully.')
        else:
            messages.error(request, 'You do not have permission to delete this feedback.')
    return redirect('Customer:user_orders')
