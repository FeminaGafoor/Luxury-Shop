# Generated by Django 4.2.6 on 2023-11-27 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_product',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
