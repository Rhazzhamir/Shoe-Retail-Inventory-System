# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Username',
                'style': 'background-color: #151f2c ;color: white',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Email',
                'style': 'background-color: #151f2c ;color: white'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set widgets for password1 and password2
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Password',
            'style': 'background-color: #151f2c ;color: white'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Confirm Password',
            'style': 'background-color: #151f2c ; color: white'
        })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Username',
            'style': 'background-color: #151f2c ; color: white'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Password',
            'style': 'background-color: #151f2c ; color: white'
        })