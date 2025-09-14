# bookings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from doctors.models import Doctor
from services.models import Service
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
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

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form})