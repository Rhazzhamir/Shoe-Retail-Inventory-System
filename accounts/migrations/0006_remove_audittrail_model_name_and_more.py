# Generated by Django 5.1.2 on 2025-01-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_audittrail_model_name_audittrail_object_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audittrail',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='audittrail',
            name='object_id',
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='action',
            field=models.CharField(choices=[('login', 'Login'), ('logout', 'Logout')], max_length=10),
        ),
    ]
