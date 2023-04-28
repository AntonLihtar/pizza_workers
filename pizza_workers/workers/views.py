from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Worker


# Create your views here.
def get_workers(request):
    workers = Worker.objects.all()
    return render(request, 'workers/workers.html', {'workers': workers})


def get_one_worker(request, id_worker):
    worker = get_object_or_404(Worker, id=id_worker)
    return render(request, 'workers/one_worker.html', {'worker': worker})



