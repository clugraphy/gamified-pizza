# Generated by Django 3.1.7 on 2021-04-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210404_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/<django.db.models.fields.CharField>'),
        ),
    ]
