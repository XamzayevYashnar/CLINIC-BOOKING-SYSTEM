# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:doctor_id>/', views.create_booking, name='create_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
]