# Generated by Django 4.2.6 on 2023-11-08 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutipleimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.products'),
        ),
    ]
