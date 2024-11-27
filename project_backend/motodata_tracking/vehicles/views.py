from django.shortcuts import render

# Create your views here.

def userDashboard(request):
    return render(request, 'vehicle-dashboard.html')

def userVehiclesPage(request):
    return render(request, 'vehicle-page.html')

def userVehiclesDetails(request):
    return render(request, 'vehicle-details.html')

def saVehiclesManagement(request):
    return render(request, 'sa-vehicle-management.html')

def saDashboard(request):
    return render(request, 'sa-dashboard.html')