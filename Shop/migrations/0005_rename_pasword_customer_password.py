# Generated by Django 4.2.20 on 2025-05-12 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='pasword',
            new_name='password',
        ),
    ]
