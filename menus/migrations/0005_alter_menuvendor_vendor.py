# Generated by Django 3.2 on 2023-03-28 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_rename_address_vendoraddress_address_line1'),
        ('menus', '0004_alter_menuvendor_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuvendor',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='vendors.vendor'),
        ),
    ]
