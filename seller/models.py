from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)  # Make it nullable

    def save(self, *args, **kwargs):
        if self.pk:  # If the category already exists, update the updated_at field
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)  # Make it nullable

    def save(self, *args, **kwargs):
        if self.pk:  # If the product already exists, update the updated_at field
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name