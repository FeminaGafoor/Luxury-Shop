# Generated by Django 4.2.6 on 2023-11-03 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_alter_user_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
