# Generated by Django 4.2.9 on 2024-02-17 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_scentprofile_alter_product_scent_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='scent_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.scentprofile'),
        ),
    ]
