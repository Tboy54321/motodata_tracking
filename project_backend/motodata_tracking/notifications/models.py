from django.db import models
from django.conf import settings
from vehicles.models import Tasks, Vehicle

# Create your models here.

READ_RECEIPT = [
    ('Read', 'Read'),
    ('Unread', 'Unread')
]

class Notification(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    service_adviser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sa_notifications", default=1)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles')
    title = models.CharField(max_length=200)
    notification_type = models.CharField(
        max_length=50,
        choices=[
            ('Job Update', 'Job Update'),
            ('Alert', 'Alert'),
            ('Service Completion', 'Service Completion'),
            ('General Information', 'General Information'),
        ],
    )
    status = models.CharField(max_length=10, choices=READ_RECEIPT, default='Unread')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.customer.username}: {self.message[:50]}"
    
    class Meta:
        ordering = ['-created_at']
