from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate , logout
from .form import CustomUserCreationForm , CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request , 'Registration successful! Please log in.')
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)

            messages.success(request , 'Login Successful')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            if user.is_superuser:
                return redirect('../../admin')
            if user.is_staff:
                return redirect('seller:seller_dashboard')
            else:
                return redirect('Customer:user_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request , 'login.html' , {'form' : form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout successful! You have been logged out.')
        return redirect('accounts:login')
    return redirect('accounts:login')

# Profile

@login_required(login_url='accounts:login')
def profile_view(request):
    return render(request , 'profile.html')


@login_required(login_url='accounts:login')
def user_profile(request):
    if request.method == 'POST':
        user = request.user
        
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        
        try:
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:User-Profile')
        except Exception as e:
            messages.error(request, f'Error updating profile: {e}')
    else:
        pass
    return render(request, 'profile.html', {'user': request.user})


# Change password
@login_required(login_url='accounts:login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password has been changed successfully.')
                return redirect('accounts:User-Profile')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'profile.html')






# Seller views

@login_required(login_url='accounts:login')
def seller_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')

        try:
            user.save()
            messages.success(request, 'Seller profile updated successfully!')
            return redirect('accounts:Seller-Profile')  
        except Exception as e:
            messages.error(request, f'Error updating seller profile: {e}')
    return render(request, 'seller_profile.html', {'user': request.user})
