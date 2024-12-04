from django.shortcuts import render
from .models import CustomerProfile
from .forms import CustomerForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

    return render(request, 'login.html')

def usersProfile(request):
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'users-profile.html', context)

def saProfile(request):
    return render(request, 'sa-profile.html')