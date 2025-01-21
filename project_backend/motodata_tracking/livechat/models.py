from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"From {self.sender} - {self.room} - {self.timestamp}"
