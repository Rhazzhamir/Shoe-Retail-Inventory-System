from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category
from .form import CategoryForm

@login_required(login_url='accounts:login')
def seller_dashboard_view(request):
    category_id = request.POST.get('category_id')  # Get category ID if available
    
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
    }
    return render(request, 'seller_dashboard.html', context)

@login_required(login_url='accounts:login')
def delete_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('seller:seller_dashboard')



@login_required(login_url='accounts:login')
def profile_view(request):
    return render(request , 'seller_profile.html')


