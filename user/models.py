from django.db import models
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)