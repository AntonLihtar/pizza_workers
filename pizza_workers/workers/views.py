from django.shortcuts import render


# Create your views here.
def workers(request):
    return render(request, 'workers/workers.html')
