# Generated by Django 4.2.6 on 2023-11-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_user_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='state',
            field=models.CharField(default=True, max_length=15),
        ),
    ]