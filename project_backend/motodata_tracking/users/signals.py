from .models import CustomerProfile
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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