from django.db import models
from django.contrib.auth.models import User
from videochat.models import Conference

# Create your models here.
class Invite(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_users')
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
