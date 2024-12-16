from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     is_service_adviser = models.BooleanField(default=False)
#     is_customer = models.BooleanField(default=False)

#     def __str__(self):
#         return self.email
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='customerprofile')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

# class CustomerProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_number = models.IntegerField()
#     address = models.TextField(max_length=100)
#     # profile_picture = 

#     def __str__(self):
#         return self.first_name
    
# class ServiceAdviserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='service_adviser_profile')
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     department = models.CharField(max_length=15)
#     phone_number = models.IntegerField()
#     # profile_picture

#     def __str__(self):
#         return self.first_name

