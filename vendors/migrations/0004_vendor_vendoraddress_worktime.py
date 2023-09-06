# Generated by Django 3.2 on 2023-02-08 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20230208_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('logo', models.ImageField(upload_to='vendors/logo')),
                ('profile_image', models.ImageField(upload_to='vendors/profile')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='vendors.city')),
            ],
        ),
        migrations.CreateModel(
            name='VendorAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=70)),
                ('address_line2', models.CharField(blank=True, max_length=50, null=True)),
                ('post_code', models.CharField(blank=True, max_length=10, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='vendors.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField(choices=[(5, 'شنبه'), (6, 'یکشنبه'), (0, 'دوشنبه'), (3, 'سه شنبه'), (2, ' چهارشنبه'), (3, 'پنجشنبه'), (4, 'جمعه')])),
                ('open_morning', models.CharField(max_length=8)),
                ('close_morning', models.CharField(max_length=8)),
                ('open_afternoon', models.CharField(max_length=8)),
                ('close_afternoon', models.CharField(max_length=8)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='open_times', to='vendors.vendor')),
            ],
            options={
                'unique_together': {('vendor', 'day')},
            },
        ),
    ]
