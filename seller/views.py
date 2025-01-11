# seller/views.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product , DeletedCategory , DeletedProduct
from .form import CategoryForm , ProductForm  
from user.models import Feedback
from django.http import JsonResponse
from .models import Product 
from user.models import Order
from django.db.models import Sum

@login_required(login_url='accounts:login')
def seller_dashboard_view(request):
    category_id = request.POST.get('category_id')  # Get category ID from POST request
    products = Product.objects.filter(seller=request.user)
    
    if request.method == 'POST':
        if category_id:  # If category_id is present, we are updating
            category = get_object_or_404(Category, id=category_id)
            form = CategoryForm(request.POST, instance=category)  # Load existing data for updating
            if form.is_valid():
                form.save()  # Update the category
                messages.success(request, 'Category updated successfully!')
                return redirect('seller:seller_dashboard')
        else:  # If no category_id, we are adding a new category
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()  # Add the new category
                messages.success(request, 'Category added successfully!')
                return redirect('seller:seller_dashboard')
    else:
        form = CategoryForm()

    feedback_list = Feedback.objects.filter(
        order__product__seller=request.user
    ).select_related(
        'user', 
        'order', 
        'order__product'
    ).order_by('-created_at')
    categories = Category.objects.all()
    total_sum = categories.count()
    total_products = products.count()  # Count the total number of products
    total_stock = sum(product.stock for product in products)
    out_of_stock = products.filter(stock=0).count()
    low_stock = products.filter(stock=1).count()
    orders = Order.objects.all()
    total_orders = orders.count()

    total_price = orders.aggregate(total=Sum('price'))['total'] or 0
    # Fetch deleted history
    deleted_categories = DeletedCategory.objects.all()
    deleted_products = DeletedProduct.objects.all()

    context = {
        'form': form,
        'categories': categories,
        'products': products,
        'total_sum': total_sum,
        'total_products': total_products,
        'total_stock': total_stock,
        'deleted_categories': deleted_categories,
        'deleted_products': deleted_products,
        'out_of_stock_count': out_of_stock,
        'low_stock_count': low_stock,
        'orders': orders,
        'feedback_list': feedback_list , 
        'total_orders' : total_orders,
        'total_price': total_price
    }
    return render(request, 'seller_dashboard.html', context)


# @login_required(login_url='accounts:login')
# def delete_category_view(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     category.delete()
#     messages.success(request, '   Category deleted successfully!')
#     return redirect('seller:seller_dashboard')

@login_required(login_url='accounts:login')
def delete_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    # Log the deleted products related to the category
    products = category.products.all()  # Get all products related to this category
    for product in products:
        DeletedProduct.objects.create(
            product_name=product.product_name,
            image=product.image,
            description=product.description,
            price=product.price,
            stock=product.stock
        )
    
    # Log the deleted category
    DeletedCategory.objects.create(category_name=category.category_name)
    # Delete the category
    category.delete()
    
    messages.success(request, 'Category and related products deleted successfully!')
    return redirect('seller:seller_dashboard')

@login_required(login_url='accounts:login')
def delete_deleted_category_view(request, category_id):
    category = get_object_or_404(DeletedCategory, id=category_id)
    category.delete()
    return JsonResponse({'success': True})



# PRODUCT
@login_required(login_url='accounts:login')
def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for image upload
        if form.is_valid():
            product = form.save(commit=False)  # Create the product instance but don't save it yet
            product.seller = request.user  # Set the seller to the currently logged-in user
            product.save()  # Now save the product
            messages.success(request, 'Product added successfully!')
            return redirect('seller:seller_dashboard')  # Redirect to the dashboard or wherever you want
    else:
        form = ProductForm()
    
    categories = Category.objects.all()  # Get categories for the dropdown
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'seller_dashboard.html', context)  # Adjust the template as needed


@login_required(login_url='accounts:login')
def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('seller:seller_dashboard')
    else:
        form = ProductForm(instance=product)
    
    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories,
        'product': product,
    }
    return render(request, 'seller_dashboard.html', context)

@login_required(login_url='accounts:login')
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Log the deleted product
    DeletedProduct.objects.create(
        product_name=product.product_name,
        image=product.image,
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    # Delete the product
    product.delete()
    
    messages.success(request, 'Product deleted successfully!')
    return redirect('seller:seller_dashboard')


@login_required(login_url='accounts:login')
def delete_deleted_product_view(request, product_id):
    product = get_object_or_404(DeletedProduct, id=product_id)
    product.delete()
    return JsonResponse({'success': True})

@login_required(login_url='accounts:login')
def profile_view(request):
    return render(request , 'seller_profile.html')


@login_required(login_url='accounts:login')
def delete_feedback(request, feedback_id):
    # Get the feedback object or return 404
    feedback = get_object_or_404(Feedback, id=feedback_id)
    
    # Check if the feedback belongs to a product sold by the current user
    if feedback.order.product.seller == request.user:
        feedback.delete()
        messages.success(request, 'Feedback deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this feedback!')
    
    return redirect('seller:seller_dashboard')

def delete_order(request, order_id):
    # Get the order or return 404
    order = get_object_or_404(Order, id=order_id)
    
    # Check if the order belongs to a product sold by the current user
    if order.product.seller == request.user:
        order.delete()
        messages.success(request, 'Order cancelled successfully!')
    else:
        messages.error(request, 'You do not have permission to cancel this order!')
    
    return redirect('seller:seller_dashboard')