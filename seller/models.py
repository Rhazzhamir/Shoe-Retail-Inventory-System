from django.db import models
from django.utils import timezone

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