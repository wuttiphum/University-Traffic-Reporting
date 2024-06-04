# Generated by Django 4.2.3 on 2023-08-26 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0007_notification_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('fristname', models.CharField(max_length=20, null=True)),
                ('lastname', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('picture', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.officer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.user')),
            ],
        ),
    ]
