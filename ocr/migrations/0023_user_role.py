# Generated by Django 4.2.3 on 2023-11-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0022_alter_report_problem_officer_alter_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
