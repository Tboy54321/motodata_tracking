from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications, name='notifcations'),
    path('sa/notifications/', views.saNotifications, name='sa-notifications'),
]