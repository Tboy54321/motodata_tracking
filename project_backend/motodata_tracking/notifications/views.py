from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def notifications(request):
    return render(request, 'notification.html')

def saNotifications(request):
    return render(request, 'sa-notification-management.html')