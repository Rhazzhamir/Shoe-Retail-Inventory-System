# Generated by Django 5.1.2 on 2025-01-10 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCancellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancel_date', models.DateTimeField(auto_now_add=True)),
                ('cancel_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.order')),
            ],
        ),
    ]
