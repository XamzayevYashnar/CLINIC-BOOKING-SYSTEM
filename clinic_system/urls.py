from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), 
    path('users/', include('users.urls')),
    path('doctors/', include('doctors.urls')),
    path('services/', include('services.urls')),
    path('bookings/', include('bookings.urls')),
]
