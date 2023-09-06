# Generated by Django 3.2 on 2023-02-12 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20230210_1107'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='order', to='customer.customeraddress'),
        ),
    ]
