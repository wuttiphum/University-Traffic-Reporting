# Generated by Django 4.2.3 on 2023-11-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0054_remove_car_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='picture_car',
            field=models.ImageField(max_length=150, null=True, upload_to='picture_car'),
        ),
    ]
