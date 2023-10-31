# Generated by Django 4.2.6 on 2023-10-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_products_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.ManyToManyField(to='items.size'),
        ),
        migrations.AlterField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(to='items.color'),
        ),
    ]
