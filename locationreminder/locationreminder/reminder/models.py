from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    target_lat = models.FloatField()
    target_lon = models.FloatField()
    radius = models.PositiveIntegerField(default=500)  # meters
    created_at = models.DateTimeField(auto_now_add=True)
    triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} @ ({self.target_lat},{self.target_lon})"
