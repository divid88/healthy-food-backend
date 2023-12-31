# Generated by Django 3.2 on 2023-04-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0007_auto_20230415_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='categories/logos/'),
        ),
        migrations.AlterField(
            model_name='foodcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/images/'),
        ),
    ]
