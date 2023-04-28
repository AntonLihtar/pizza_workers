from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index/index.html')


def get_date(request, mon, day):
    return HttpResponse(f'Дата: {day}, {mon}')
