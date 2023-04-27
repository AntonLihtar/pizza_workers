# Generated by Django 4.2 on 2023-04-27 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tow_trucks', '0003_alter_car_drivers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(blank=True, to='tow_trucks.driver'),
        ),
        migrations.AlterField(
            model_name='car',
            name='garage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tow_trucks.garage'),
        ),
    ]
