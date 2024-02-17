from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

# Create your views here.

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking request received! Await confirmation'
            )
            form = BookingForm()
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking.html', {'form': form})