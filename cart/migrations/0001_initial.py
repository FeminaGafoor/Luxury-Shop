# Generated by Django 4.2.6 on 2023-11-04 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0009_alter_user_profile_image'),
        ('items', '0006_color_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('quantity', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user_profile')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.products')),
                ('single_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.product_variant')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]