from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Notification

def searchQuery(request, user_type='customer'):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # vehicles = Vehicle.objects.filter(owner=request.user)
    if user_type == 'customer':
        notification = Notification.objects.filter(
        Q(customer=request.user) & 
            (
            Q(title__icontains=search_query) | 
            Q(message__icontains=search_query)
            )
        )
    elif user_type == 'service_adviser':
        notification = Notification.objects.filter(
        Q(service_adviser=request.user) & 
            (
            Q(title__icontains=search_query) | 
            Q(message__icontains=search_query)
            )
        )
    return search_query, notification

def paginatePage(queryset, results, page):

    paginator = Paginator(queryset, results)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        queryset = paginator.page(page)
    except EmptyPage:
        page = Paginator.num_pages
        queryset = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 4)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages
    
    custom_range = range(left_index, right_index)
    # print(custom_range)
    return custom_range, queryset