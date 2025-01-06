from django.shortcuts import render
from .models import Notification

# Create your views here.

from django.http import HttpResponse

def notifications(request):
    notification_list = Notification.objects.filter(customer=request.user)
    context = {'notification_list': notification_list}
    return render(request, 'notification.html', context)

def saNotifications(request):
    return render(request, 'sa-notification-management.html')