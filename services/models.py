# services/models.py
from django.db import models
from doctors.models import Doctor

class Service(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.doctor.user.first_name}"
