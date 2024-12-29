from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.loginAccount, name='login'),
    path('signup/', views.signUpUser, name='signupUser'),
    path('delete-account/', views.deleteAccount, name='delete-account'),
    path('signupSA/', views.signupSA, name='signupSA'),
    path('logout/', views.logoutAccount, name='logout'),
    path('profile/', views.usersProfile, name='profile'),
    path('sa/profile/', views.saProfile, name='sa-profile'),
    path('edit-user/', views.userEditProfile, name='edit-user'),
    path('edit-sa/', views.saEditProfile, name='edit-profile'),
]