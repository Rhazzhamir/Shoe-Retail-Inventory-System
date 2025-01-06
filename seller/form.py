from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']  
        labels = {
            'category_name': 'Category', 
        }
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control' ,
                'id': 'categoryName',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
        }
