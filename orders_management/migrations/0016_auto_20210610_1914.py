# Generated by Django 3.1.7 on 2021-06-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_management', '0015_auto_20210610_0327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created', 'first_name', 'last_name')},
        ),
        migrations.AlterField(
            model_name='order',
            name='nickname',
            field=models.CharField(max_length=40),
        ),
    ]
