# Generated by Django 4.2.6 on 2023-10-15 04:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='in_stock',
        ),
        migrations.AddField(
            model_name='category',
            name='create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='update',
            field=models.DateField(auto_now=True),
        ),
    ]
