# Generated by Django 5.0.3 on 2024-06-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_alter_producttransactions_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransactions',
            name='recipient',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
