# Generated by Django 5.1.4 on 2025-04-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_car_urgent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='mileage',
        ),
        migrations.AddField(
            model_name='car',
            name='registraton',
            field=models.CharField(default='Not Available', max_length=100),
            preserve_default=False,
        ),
    ]
