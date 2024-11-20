from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicles, name='vehicles'),
    path('page/', views.vehiclesPage, name='vehicles-page'),
    path('details/', views.vehiclesDetails, name='vehicles-details'),
]