# Generated by Django 5.1.2 on 2025-01-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_category_deleted_at_product_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
    ]
