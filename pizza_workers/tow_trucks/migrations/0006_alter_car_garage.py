# Generated by Django 4.2 on 2023-04-27 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tow_trucks', '0005_alter_car_garage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='garage',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), to='tow_trucks.garage'),
        ),
    ]
