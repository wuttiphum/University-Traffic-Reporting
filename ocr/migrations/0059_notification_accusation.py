# Generated by Django 4.2.3 on 2023-11-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0058_notification_stack'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='accusation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
