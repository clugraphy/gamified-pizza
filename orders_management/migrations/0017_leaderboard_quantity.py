# Generated by Django 3.1.7 on 2021-06-23 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders_management', '0016_auto_20210610_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='quantity',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, to='orders_management.orderitem'),
        ),
    ]
