from django import forms
from .models import *

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'  # Or specify the fields you want in the form

class AppointmentForm(forms.ModelForm):
     class Meta:
         model = Appointment
         fields = '__all__'

class MedicalRecordForm(forms.ModelForm): # Form for creating/editing Medical Records
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingHotel
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class ReservForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }