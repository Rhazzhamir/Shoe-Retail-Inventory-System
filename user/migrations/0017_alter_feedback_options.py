# Generated by Django 5.1.2 on 2025-01-10 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-created_at']},
        ),
    ]
