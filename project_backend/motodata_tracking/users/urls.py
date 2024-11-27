from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('profile/', views.usersProfile),
    path('sa/profile/', views.saProfile)
]