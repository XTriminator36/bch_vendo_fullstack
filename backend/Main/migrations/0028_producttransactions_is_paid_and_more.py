# Generated by Django 5.0.3 on 2024-06-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_remove_producttransactions_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransactions',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producttransactions',
            name='paid_timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='producttransactions',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
