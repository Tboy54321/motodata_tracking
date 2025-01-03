from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from users.views import role_required

# Create your views here.

@login_required(login_url='login')
@role_required('customer')
def userDashboard(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    context = {'vehicles': vehicles}
    return render(request, 'vehicle-dashboard.html', context)

@login_required(login_url='login')
@role_required('customer')
def userVehiclesPage(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    context = {'vehicles': vehicles}
    return render(request, 'vehicle-page.html', context)

@login_required(login_url='login')
@role_required('customer')
def userVehiclesDetails(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    context = {'vehicle': vehicle}
    return render(request, 'vehicle-details.html', context)


@login_required(login_url='login')
@role_required('service_adviser')
def saVehiclesManagement(request):
    return render(request, 'sa-vehicle-management.html')

@login_required(login_url='login')
@role_required('service_adviser')
def saDashboard(request):
    return render(request, 'sa-dashboard.html')