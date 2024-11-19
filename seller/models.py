from django.db import models

# Create your models here.
# class category(models.Model):
#     categoryName = models.charfield(max_length = 255)

#     def __str__(self):
#         return self.categoryName
    
# class product(models.Model):
#     category = models.ForeignKey(category, related_name = 'seller' , on_delete=models.CASCADE)
#     Product_Name = models.CharField(max_length=255)
#     Price = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add = True)
    
#     def __str__(self):
#         return self.Product_Name