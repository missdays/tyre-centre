from django.shortcuts import render
from .models import Booking


# Create your views here.

def my_booking(request):
    booking = Booking.objects.all()
    return render(request, 'booking/booking.html', {"booking": booking})