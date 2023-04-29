from django.http import HttpResponse
from django.shortcuts import render

from .generator_names import create_name
from .models import Product
import random

"""Эта страница заполнит бд на 100 записей
    create_name - генерит имена от 3 до 7 символов в длину(дефолт)
    """


def create_price():
    return random.randint(5, 500)


def create_bd():
    count = 100
    while count > 0:
        a = Product(name=create_name(), price=create_price(), quantity=random.randint(1, 100))
        a.save()
        print(a)
        count -= 1


def get_all_products(request):
    # create_bd()  # активировав метод добавим записи в таблицу
    products = Product.objects.all()
    return render(request, 'product/products.html', {'products': products})
