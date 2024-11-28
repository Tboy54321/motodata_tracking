from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('profile/', views.usersProfile, name='profile'),
    path('sa/profile/', views.saProfile, name='sa-profile')
]