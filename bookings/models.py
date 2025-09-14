# bookings/models.py
from django.db import models
from users.models import User
from doctors.models import Doctor
from services.models import Service

class Booking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[('pending','Pending'),('confirmed','Confirmed'),('canceled','Canceled')],
        default='pending'
    )

    def __str__(self):
        return f"{self.patient.username} -> {self.doctor.user.username} on {self.date}"
