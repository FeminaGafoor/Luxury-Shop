# Generated by Django 4.2.6 on 2023-11-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_user_profile_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='state',
            field=models.CharField(default=True, max_length=15, null=True),
        ),
    ]