# Generated by Django 4.2.3 on 2023-08-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0010_alter_user_address_alter_user_age_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
