# Generated by Django 4.2.6 on 2023-10-18 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_products_size_alter_products_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.RemoveField(
            model_name='products',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='size',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
        migrations.AddField(
            model_name='products',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Product_variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.CharField(blank=True, max_length=100)),
                ('colors', models.ManyToManyField(to='items.color')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='items.products')),
                ('size', models.ManyToManyField(to='items.size')),
            ],
        ),
        migrations.AddField(
            model_name='productimage',
            name='variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.product_variant'),
        ),
    ]