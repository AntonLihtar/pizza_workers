# Generated by Django 4.2 on 2023-04-23 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=12, unique=True)),
                ('sex', models.CharField(choices=[('f', 'Женщина'), ('m', 'Мужчина')], default='m', max_length=1)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(70)])),
                ('experience', models.CharField(choices=[('<5', 'Меньше 6 месяцев'), ('>5', 'От 6 месяцев до 1 года'), ('>1', 'От 1 года до 3'), ('>3', 'Больше 3х лет')], default='<5', max_length=2)),
                ('doc', models.TextField(blank=True)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]