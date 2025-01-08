from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('feedback/create/', views.createFeedback, name='create-feedback'),
]