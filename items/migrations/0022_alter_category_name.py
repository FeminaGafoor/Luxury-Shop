# Generated by Django 4.2.6 on 2023-10-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0021_alter_category_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
