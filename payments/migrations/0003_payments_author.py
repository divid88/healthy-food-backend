# Generated by Django 3.2 on 2023-02-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20230213_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
