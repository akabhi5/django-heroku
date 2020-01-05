from django.shortcuts import render
from testapp.models import Demo

def index(request):
    return render(request, 'index.html')

def demo_view(request):
    data = Demo.objects.all()
    return render(request, 'demo.html', {'data': data})
