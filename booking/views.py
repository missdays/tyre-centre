from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django import forms
from .forms import BookingForm
from .models import Booking

# Create your views here.


@login_required
def bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(
        request,
        'booking/booking.html',
        {'user_bookings': user_bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking request received! Await confirmation.'
            )
            return redirect('booking')
    else:
        form = BookingForm(initial={'user': request.user})
        form.fields['user'].widget = forms.HiddenInput()
        form.fields['status'].widget = forms.HiddenInput()

    return render(request, 'booking/create_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.status in ['Cancelled', 'Confirmed']:
        messages.error(
            request,
            "Cannot delete a cancelled or confirmed booking.")
        return redirect('booking')

    booking.delete()
    messages.success(request, "Booking deleted successfully.")
    return redirect('booking')


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.status in ['Cancelled', 'Confirmed']:
        messages.error(
            request,
            "Cannot edit a cancelled or confirmed booking.")
        return redirect('booking')

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking updated! Await confirmation.'
            )
            return redirect('booking')
    else:
        form = BookingForm(instance=booking)
        form.fields['user'].widget = forms.HiddenInput()
        form.fields['status'].widget = forms.HiddenInput()

    return render(
        request,
        'booking/create_booking.html',
        {'form': form, 'booking_id': booking_id})
