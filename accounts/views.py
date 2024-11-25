from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate , logout
from .form import CustomUserCreationForm , CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
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
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('Customer:user_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request , 'login.html' , {'form' : form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:login')

# Profile

@login_required(login_url='accounts:login')
def profile_view(request):
    return render(request , 'profile.html')


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:User-Profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


