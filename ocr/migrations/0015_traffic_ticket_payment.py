# Generated by Django 4.2.3 on 2023-09-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0014_alter_officer_picture_alter_user_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='traffic_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accusation', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('picture_evidence', models.CharField(max_length=200, null=True)),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.officer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.user')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_evidence', models.ImageField(max_length=10, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.user')),
            ],
        ),
    ]
