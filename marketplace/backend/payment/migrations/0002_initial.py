# Generated by Django 5.0.3 on 2024-03-16 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        ('productsapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapi.products', verbose_name='Товар'),
        ),
    ]