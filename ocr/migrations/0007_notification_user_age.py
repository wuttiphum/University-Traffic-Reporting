# Generated by Django 4.2.3 on 2023-08-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0006_user_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=15, null=True)),
                ('picture', models.FileField(max_length=20, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
