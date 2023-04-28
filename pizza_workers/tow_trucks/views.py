from django.shortcuts import render

from .models import Car


def get_all_cars(request):
    cars = Car.objects.all()
    return render(request, 'tow_trucks/all_cars.html', {'cars': cars})
