from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vehicles(request):
    return render(request, 'vehicle-dashboard.html')