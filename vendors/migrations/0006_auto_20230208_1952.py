# Generated by Django 3.2 on 2023-02-08 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_alter_worktime_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendoraddress',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendoraddress',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='worktime',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worktime',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
