from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate , logout
from .form import CustomUserCreationForm , CustomAuthenticationForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Customer:user_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect('Customer:user_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request , 'login.html' , {'form' : form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:login')


    