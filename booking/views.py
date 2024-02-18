from django.shortcuts import render
from django.contrib import messages
from django import forms
from .forms import BookingForm

# Create your views here.

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking request received! Await confirmation'
            )
            form = BookingForm(initial={'user': request.user})
            form.fields['user'].widget = forms.HiddenInput()
            form.fields['status'].widget = forms.HiddenInput()
    else:
        form = BookingForm(initial={'user': request.user})
        form.fields['user'].widget = forms.HiddenInput()
        form.fields['status'].widget = forms.HiddenInput()
    
    return render(request, 'booking/booking.html', {'form': form})