# Generated by Django 4.2.9 on 2024-02-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='scent_profile',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
