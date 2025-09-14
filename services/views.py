# services/views.py
from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})
