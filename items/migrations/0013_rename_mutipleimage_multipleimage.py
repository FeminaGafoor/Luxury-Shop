# Generated by Django 4.2.6 on 2023-11-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_remove_mutipleimage_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MutipleImage',
            new_name='MultipleImage',
        ),
    ]
