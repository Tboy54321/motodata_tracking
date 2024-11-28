from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def usersProfile(request):
    return render(request, 'users-profile.html')

def saProfile(request):
    return render(request, 'sa-profile.html')