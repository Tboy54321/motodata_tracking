from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     is_service_adviser = models.BooleanField(default=False)
#     is_customer = models.BooleanField(default=False)

#     def __str__(self):
#         return self.email
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.email)

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

# @receiver(post_save, sender=CustomerProfile)  
def create_user_for_customer_profile(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create(
            username=f"{instance.first_name.lower()}.{instance.last_name.lower()}",
            first_name=instance.first_name or "",
            last_name=instance.last_name or "",
            email=instance.email or "",
            password=make_password("defaultpassword123")
        )
        
        instance.user = user
        instance.save()

def delete_user_for_customer_profile(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()

post_save.connect(create_user_for_customer_profile, sender=CustomerProfile)
post_delete.connect(delete_user_for_customer_profile, sender=CustomerProfile)