from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime

# Create your models here.
class otps(models.Model):
    email=models.EmailField(max_length=100)
    otp=models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(minutes=5))

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return self.email