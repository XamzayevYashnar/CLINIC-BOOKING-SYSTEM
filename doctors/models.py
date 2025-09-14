# doctors/models.py
from django.db import models
from users.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
