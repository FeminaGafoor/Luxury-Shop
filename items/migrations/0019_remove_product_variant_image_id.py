# Generated by Django 4.2.6 on 2023-11-21 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_alter_banner_partners_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_variant',
            name='image_id',
        ),
    ]