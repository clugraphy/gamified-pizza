# Generated by Django 3.1.7 on 2021-06-10 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders_management', '0013_auto_20210610_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='nickname',
        ),
        migrations.AddField(
            model_name='order',
            name='nickname',
            field=models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]