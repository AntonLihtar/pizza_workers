# Generated by Django 4.2 on 2023-04-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
