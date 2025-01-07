from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category , Product
from .form import CategoryForm , ProductForm

# CATEGORY
@login_required(login_url='accounts:login')
def seller_dashboard_view(request):
    category_id = request.POST.get('category_id')  # Get category ID if available
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

    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories,
        'products': products,
    }
    return render(request, 'seller_dashboard.html', context)

@login_required(login_url='accounts:login')
def delete_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('seller:seller_dashboard')

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
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('seller:seller_dashboard')
    return render(request, 'seller_dashboard.html')

@login_required(login_url='accounts:login')
def profile_view(request):
    return render(request , 'seller_profile.html')


