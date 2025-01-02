from django.db import models
from django.conf import settings

# Create your models here.

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vehicles")
    registration_number = models.CharField(max_length=50, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    vin = models.CharField(max_length=100)
    plate = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    condition = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed'),
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"
    

# class JobCard(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="job_cards")
#     service_advisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="advised_jobs")
#     description = models.TextField()  # Details about the job
#     technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="assigned_jobs")
#     status = models.CharField(
#         max_length=50,
#         choices=[
#             ('Not Started', 'Not Started'),
#             ('In Progress', 'In Progress'),
#             ('Completed', 'Completed'),
#         ],
#         default='Not Started'
#     )
#     start_time = models.DateTimeField(null=True, blank=True)  # When technician starts the job
#     end_time = models.DateTimeField(null=True, blank=True)  # When job is marked as completed
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"JobCard for {self.vehicle.registration_number} - {self.status}"
