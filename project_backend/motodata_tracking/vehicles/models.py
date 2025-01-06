from django.db import models
from django.conf import settings

# Create your models here.

STATUS_CHOICES = [
    ('Pending', 'pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vehicles")
    registration_number = models.CharField(max_length=50, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    vin = models.CharField(max_length=100)
    plate = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    condition = models.TextField(max_length=500)
    concern = models.TextField(default='None', max_length=1000)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    # NEED TO ALLOW THE SERVICE ADVISER TO GET TO ADD THE TASK AND UPDATE THE STATUS
    progress = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"
    

class Tasks(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)    
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"