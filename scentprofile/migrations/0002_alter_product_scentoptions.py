# Generated by Django 4.2.9 on 2024-02-17 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scentprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='scentoptions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scentprofile.scentprofile'),
        ),
    ]
