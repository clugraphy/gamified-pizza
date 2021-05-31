# Generated by Django 3.1.7 on 2021-05-30 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_product_pizzereum'),
        ('orders_management', '0002_orderitem_pizzereum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='orders_management.order')),
                ('last_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last', to='orders_management.order')),
                ('pizzereum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='orders.product')),
            ],
        ),
    ]
