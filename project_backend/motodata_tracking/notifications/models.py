# from django.db import models
# from django.conf import settings
# from vehicles.models import JobCard

# # Create your models here.
# class Notification(models.Model):
#     recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
#     job_card = models.ForeignKey(JobCard, on_delete=models.CASCADE, related_name="notifications")
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Notification for {self.recipient.username}: {self.message[:50]}"
