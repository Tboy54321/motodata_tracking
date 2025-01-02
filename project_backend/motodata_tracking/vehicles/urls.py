from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.userDashboard, name='vehicle-dashboard'),
    path('vehicle-page/', views.userVehiclesPage, name='vehicles-page'),
    path('vehicle-details/<str:pk>', views.userVehiclesDetails, name='vehicles-details'),
    path('sa/vehicle-management/', views.saVehiclesManagement, name='vehicles-management'),
    path('sa/dashboard/', views.saDashboard, name='sa-dashboard'),
]