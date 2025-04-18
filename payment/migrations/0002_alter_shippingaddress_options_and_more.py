# Generated by Django 5.0.4 on 2024-12-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping Address'},
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='adress1',
            new_name='Shipping_adress1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='Shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='Shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='email',
            new_name='Shipping_email',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='Shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='phone',
            new_name='Shipping_state',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='user',
            new_name='Shipping_user',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='Shipping_zipcode',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='adress2',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='old_cart',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='Shipping_adress2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
