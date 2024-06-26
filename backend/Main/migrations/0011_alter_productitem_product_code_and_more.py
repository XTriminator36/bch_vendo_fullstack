# Generated by Django 5.0.3 on 2024-03-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_alter_productitem_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='product_code',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
