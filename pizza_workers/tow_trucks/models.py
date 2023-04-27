from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Doc(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)])
    number = models.CharField(max_length=5, default='00000')


class Driver(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)])
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])


class Spares(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)])
    document = models.OneToOneField(Doc, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)
    spares = models.ForeignKey(Spares, on_delete=models.CASCADE, null=True)
