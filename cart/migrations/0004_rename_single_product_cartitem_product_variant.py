# Generated by Django 4.2.6 on 2023-11-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cartitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='single_product',
            new_name='product_variant',
        ),
    ]
