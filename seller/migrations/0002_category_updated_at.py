# Generated by Django 5.1.2 on 2025-01-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]