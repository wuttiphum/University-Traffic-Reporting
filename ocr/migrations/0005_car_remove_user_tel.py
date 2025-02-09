# Generated by Django 4.2.3 on 2023-08-26 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0004_officer'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=15, null=True)),
                ('cc_type', models.CharField(max_length=10, null=True)),
                ('color', models.CharField(max_length=20, null=True)),
                ('license_plate', models.CharField(max_length=20, null=True)),
                ('province', models.CharField(max_length=50, null=True)),
                ('picture', models.FileField(max_length=20, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Tel',
        ),
    ]
