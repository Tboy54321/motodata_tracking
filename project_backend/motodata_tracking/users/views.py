from django.shortcuts import render
from .models import CustomerProfile
from .forms import CustomerForm

# Create your views here.

def login(request):
    return render(request, 'login.html')

def usersProfile(request):
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'users-profile.html', context)

def saProfile(request):
    return render(request, 'sa-profile.html')