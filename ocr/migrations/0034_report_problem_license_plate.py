# Generated by Django 4.2.3 on 2023-11-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0033_officer_tal'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_problem',
            name='license_plate',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
