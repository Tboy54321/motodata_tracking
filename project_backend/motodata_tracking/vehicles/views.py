from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def userDashboard(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'vehicle-dashboard.html', context)

def userVehiclesPage(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'vehicle-page.html', context)

def userVehiclesDetails(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    context = {'vehicle': vehicle}
    return render(request, 'vehicle-details.html', context)

def saVehiclesManagement(request):
    return render(request, 'sa-vehicle-management.html')

def saDashboard(request):
    return render(request, 'sa-dashboard.html')