# Generated by Django 3.2 on 2023-02-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_vendor_vendoraddress_worktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(5, 'شنبه'), (6, 'یکشنبه'), (0, 'دوشنبه'), (1, 'سه شنبه'), (2, ' چهارشنبه'), (3, 'پنجشنبه'), (4, 'جمعه')]),
        ),
    ]
