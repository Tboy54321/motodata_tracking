from django.urls import path
from . import views

urlpatterns = [
    path('', views.userDashboard, name='dashboard'),
    path('vehicle-page/', views.userVehiclesPage, name='vehicles-page'),
    path('vehicle-details/', views.userVehiclesDetails, name='vehicles-details'),
    path('sa/vehicle-management/', views.saVehiclesManagement, name='vehicles-management'),
    path('sa/', views.saDashboard, name='sa-dashboard'),
]