from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def users(request):
    return render(request, 'login.html')