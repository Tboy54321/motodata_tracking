from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Vehicle
from users.views import role_required
from .utils import paginatePage, searchQuery

# Create your views here.

@login_required(login_url='login')
@role_required('customer')
def userDashboard(request):
    page= request.GET.get('page')
    results = 3
    search_query, vehicles = searchQuery(request, user_type='owner')
    custom_range, vehicles = paginatePage(vehicles, results, page)

    context = {'vehicles': vehicles, 
               'search_query': search_query, 'custom_range': custom_range}
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
    tasks = vehicle.tasks.all()
    context = {'vehicle': vehicle, 'tasks': tasks}
    return render(request, 'vehicle-details.html', context)


@login_required(login_url='login')
@role_required('service_adviser')
def saVehiclesManagement(request):
    # vehicles = Vehicle.objects.filter(service_adviser=request.user)
    search_query, vehicles = searchQuery(request, user_type='service_adviser')
    context = {'vehicles': vehicles, "search_query": search_query}
    return render(request, 'sa-vehicle-management.html', context)

@login_required(login_url='login')
@role_required('service_adviser')
def saDashboard(request):
    vehicles = Vehicle.objects.filter(service_adviser=request.user).order_by('-created_at')[:3]
    in_progress_jobs = Vehicle.objects.filter(service_adviser=request.user, status='In Progress')
    completed_jobs = Vehicle.objects.filter(service_adviser=request.user, status='Completed')
    total_vehicles = Vehicle.objects.filter(service_adviser=request.user).count()
    context = {
        'vehicles': vehicles,
        "total_vehicles": total_vehicles,
        'in_progress_jobs': in_progress_jobs,
        'completed_jobs': completed_jobs
        }
    return render(request, 'sa-dashboard.html', context)