# Generated by Django 5.0.3 on 2024-06-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0025_delete_bchvalue_producttransactions_item_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransactions',
            name='product_code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='producttransactions',
            name='bch_value',
            field=models.FloatField(default=0, null=True),
        ),
    ]
