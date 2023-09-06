# Generated by Django 3.2 on 2023-02-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='days',
            field=models.PositiveSmallIntegerField(choices=[(1, 'شنبه'), (2, 'یکشنبه'), (3, 'دوشنبه'), (6, 'سه شنبه'), (5, ' چهارشنبه'), (6, 'پنجشنبه'), (7, 'جمعه')]),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='time_close',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='time_open',
            field=models.CharField(max_length=8),
        ),
    ]