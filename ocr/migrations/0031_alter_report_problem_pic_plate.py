# Generated by Django 4.2.3 on 2023-11-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0030_payment_price_alter_payment_photo_evidence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_problem',
            name='pic_plate',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
