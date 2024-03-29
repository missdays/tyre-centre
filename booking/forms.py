from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'booking_date_and_time', 'status', 'observation']
        widgets = {
            'booking_date_and_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}),
        }
