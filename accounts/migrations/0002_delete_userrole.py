# Generated by Django 5.1.2 on 2025-01-03 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]
