# Generated by Django 5.0.4 on 2025-01-27 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address',
            new_name='Shipping_adress',
        ),
    ]
