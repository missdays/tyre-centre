from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django import forms
from .forms import BookingForm
from .models import Booking

# Create your views here.
def bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking.html', {'user_bookings': user_bookings})

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
    
    return render(request, 'booking/create_booking.html', {'form': form})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Booking deleted successfully.")
    return redirect('booking')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm(instance=booking)
    form.fields['user'].widget = forms.HiddenInput()
    form.fields['status'].widget.attrs['disabled'] = True
    return render(request, 'booking/create_booking.html', {'form': form, 'booking_id': booking_id})