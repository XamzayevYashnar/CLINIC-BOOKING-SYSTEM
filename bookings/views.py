# bookings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from doctors.models import Doctor
from services.models import Service
from django import forms
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['doctor', 'service', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = timezone.now().date()
        self.fields['date'].widget.attrs['min'] = today  
        self.fields['time'].widget.attrs['min'] = "09:00"
        self.fields['time'].widget.attrs['max'] = "20:00"
        self.fields['time'].widget.attrs['step'] = 900 


@login_required
def create_booking(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.patient = request.user
            booking.doctor = doctor
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form, 'doctor': doctor})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(patient=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
