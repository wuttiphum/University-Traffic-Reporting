# Generated by Django 4.2.3 on 2023-11-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0040_notification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_discipline',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
