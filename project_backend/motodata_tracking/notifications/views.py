from django.shortcuts import render
from .models import Notification
from users.views import role_required
from django.contrib.auth.decorators import login_required
from .utils import paginatePage, searchQuery

# Create your views here.

from django.http import HttpResponse

@login_required(login_url='login')
@role_required('customer')
def notifications(request):
    page = request.GET.get('page')
    results = 3
    # notification_list = Notification.objects.filter(customer=request.user)
    search_query, notification_list = searchQuery(request)
    custom_range, notification_list = paginatePage(notification_list, results, page)

    context = {'notification_list': notification_list, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'notification.html', context)

@login_required(login_url='login')
@role_required('service_adviser')
def saNotifications(request):
    return render(request, 'sa-notification-management.html')