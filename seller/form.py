from django import forms
from .models import Category , Product

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
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'stock', 'image', 'category']
        labels = {
            'product_name': 'Product Name',
            'description': 'Description',
            'price': 'Price',
            'stock': 'Stock',
            'image': 'Image',
            'category': 'Category',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'productName',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'productDescription',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'productPrice',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'productStock',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'productImage',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'productCategory',
                'style': 'background-color: #151f2c; color: white;',
                'required': True,
            }),
        }