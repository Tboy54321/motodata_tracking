from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_service_adviser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.TextField(max_length=100)
    # profile_picture = 

    def __str__(self):
        return self.first_name
    
class ServiceAdviserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='service_adviser_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=15)
    phone_number = models.IntegerField()
    # profile_picture

    def __str__(self):
        return self.first_name
    