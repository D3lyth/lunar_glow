# Generated by Django 4.2.9 on 2024-02-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_scent_profile'),
        ('scentprofile', '0003_productscent_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productscent',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
