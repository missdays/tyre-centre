from . import views
from django.urls import path

urlpatterns = [
    path('<int:booking_id>/delete/', views.delete_booking, name='booking_delete'),
    path('<int:booking_id>/edit/', views.edit_booking, name='booking_edit'),
    path('create_booking', views.create_booking, name='create_booking'),
    path('', views.bookings, name='booking'),
]