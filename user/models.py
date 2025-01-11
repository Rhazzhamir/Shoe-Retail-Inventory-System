# user/models.py
from django.db import models
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default='pending')  # Default status is 'pending'

class OrderCancellation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    cancel_date = models.DateTimeField(auto_now_add=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)

# user/models.py
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} for Order {self.order.id}"
