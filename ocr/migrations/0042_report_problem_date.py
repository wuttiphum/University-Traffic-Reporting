# Generated by Django 4.2.3 on 2023-11-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0041_student_discipline_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_problem',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
