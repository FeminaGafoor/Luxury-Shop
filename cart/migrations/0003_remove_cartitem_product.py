# Generated by Django 4.2.6 on 2023-11-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_remove_cartitem_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
    ]
