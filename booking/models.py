from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date_and_time = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username}"
