# Generated by Django 4.2 on 2023-04-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tow_trucks', '0002_garage_remove_car_spares_delete_spares_car_garage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(blank=True, null=True, to='tow_trucks.driver'),
        ),
    ]
