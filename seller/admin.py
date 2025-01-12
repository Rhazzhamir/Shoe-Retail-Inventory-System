from django.contrib import admin
from .models import Category, Product, DeletedCategory, DeletedProduct
from user.models import Order , Feedback

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'created_at', 'updated_at')

class DeletedCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'deleted_at')

class DeletedProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'deleted_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user' ,'product' , 'quantity' , 'total_price' , 'order_date' , 'order_status' )

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('order' , 'feedback_text' , 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(DeletedCategory, DeletedCategoryAdmin)
admin.site.register(DeletedProduct, DeletedProductAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(Feedback , FeedbackAdmin)
