# Generated by Django 4.2.6 on 2023-11-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_mutipleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_variant',
            name='image_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
