# Generated by Django 4.0.4 on 2022-04-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vehicle_type_delete_vehicletype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='return_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='days',
            field=models.IntegerField(default=1),
        ),
    ]