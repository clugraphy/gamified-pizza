# Generated by Django 3.1.7 on 2021-04-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/<django.db.models.fields.SlugField>'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('large', 'Large'), ('small', 'Small')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
