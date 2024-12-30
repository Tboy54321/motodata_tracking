from django.db import models
from django.conf import settings
from ..vehicles.models import Workshop 
# Create your models here.

class Feedback(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedbacks")
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name="feedbacks")
    rating = models.PositiveIntegerField()  # e.g., 1-5
    comment = models.TextField(null=True, blank=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.customer.username} for {self.workshop.name}"
