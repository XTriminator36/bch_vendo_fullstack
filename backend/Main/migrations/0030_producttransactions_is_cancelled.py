# Generated by Django 5.0.3 on 2024-06-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0029_producttransactions_total_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransactions',
            name='is_cancelled',
            field=models.BooleanField(null=True),
        ),
    ]