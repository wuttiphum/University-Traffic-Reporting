# Generated by Django 4.2.3 on 2024-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0069_alter_user_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
