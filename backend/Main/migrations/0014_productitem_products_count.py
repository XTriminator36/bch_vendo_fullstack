# Generated by Django 5.0.3 on 2024-03-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_productitem_bch_vendo'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='products_count',
            field=models.IntegerField(default=0),
        ),
    ]
