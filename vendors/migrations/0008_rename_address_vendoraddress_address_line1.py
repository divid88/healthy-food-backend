# Generated by Django 3.2 on 2023-02-09 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0007_rename_address_line1_vendoraddress_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendoraddress',
            old_name='address',
            new_name='address_line1',
        ),
    ]
