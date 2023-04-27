from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Doc(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)])
    number = models.CharField(max_length=5, default='00000')

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)])
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])

    def __str__(self):
        return f'{self.name}'


class Garage(models.Model):
    name = models.CharField(max_length=20)
    size_box = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)])
    document = models.OneToOneField(Doc, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, blank=True)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
