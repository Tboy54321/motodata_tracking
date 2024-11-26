from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vehicles(request):
    return render(request, 'vehicle-dashboard.html')

def vehiclesPage(request):
    return render(request, 'vehicle-page.html')

def vehiclesDetails(request):
    return render(request, 'vehicle-details.html')

def saVehiclesManagement(request):
    return render(request, 'sa-vehicle-management.html')