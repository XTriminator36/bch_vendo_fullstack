# Generated by Django 5.0.3 on 2024-03-26 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_productitem_products_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='products_count',
        ),
    ]