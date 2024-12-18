from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signUpUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.usersProfile, name='profile'),
    path('edit/', views.editUser, name='edit'),
    
    path('sa/profile/', views.saProfile, name='sa-profile'),
]