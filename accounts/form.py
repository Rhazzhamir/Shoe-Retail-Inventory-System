# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm  text-light border-primary',
                'placeholder': 'Username',
                'style': 'background-color: #151f2c; ',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm text-light border-primary',
                'placeholder': 'Email',
                'style': 'background-color: #151f2c; '
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set widgets for password1 and password2
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm text-light border-primary',
            'placeholder': 'Password',
            'style': 'background-color: #151f2c; '
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm text-light border-primary',
            'placeholder': 'Confirm Password',
            'style': 'background-color: #151f2c; '
        })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control form-control-sm text-light border-primary',
            'placeholder': 'Username',
            'style': 'background-color: #151f2c ; '
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm text-light border-primary',
            'placeholder': 'Password',
            'style': 'background-color: #151f2c ; '
        })