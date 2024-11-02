from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  # For class-based views
from django.views import View # Base class for class-based views
from .models import *
from .forms import *



class HomeView(View):  # Class-based view for the home page
    def get(self, request):
        return render(request, 'clinic/home.html')


class PetCreateView(LoginRequiredMixin, View): # Requires login
    def get(self, request):
        form = PetForm()
        return render(request, 'clinic/pet_form.html', {'form': form})

    def post(self, request):
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save()
            return redirect('pet_detail', pk=pet.pk)
        return render(request, 'clinic/pet_form.html', {'form': form})



class PetDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        appointments = Appointment.objects.filter(pet=pet).order_by('-date')
        medical_records = MedicalRecord.objects.filter(pet=pet).order_by('-date')
        return render(request, 'clinic/pet_detail.html', {'pet': pet, 'appointments': appointments, 'medical_records': medical_records})



class AppointmentCreateView(LoginRequiredMixin, View):
    def get(self, request, pet_pk):
        pet = get_object_or_404(Pet, pk=pet_pk)
        form = AppointmentForm()
        return render(request, 'clinic/appointment_form.html', {'form': form, 'pet': pet})

    def post(self, request, pet_pk):
        pet = get_object_or_404(Pet, pk=pet_pk)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.pet = pet
            appointment.save()
            return redirect('pet_detail', pk=pet_pk)
        return render(request, 'clinic/appointment_form.html', {'form': form, 'pet': pet})




class MedicalRecordCreateView(LoginRequiredMixin, View):
    def get(self, request, pet_pk, appointment_pk=None):
        pet = get_object_or_404(Pet, pk=pet_pk)
        appointment = get_object_or_404(Appointment, pk=appointment_pk) if appointment_pk else None
        form = MedicalRecordForm()
        return render(request, 'clinic/medical_record_form.html', {'form': form, 'pet': pet, 'appointment': appointment})


    def post(self, request, pet_pk, appointment_pk=None):
        pet = get_object_or_404(Pet, pk=pet_pk)
        appointment = get_object_or_404(Appointment, pk=appointment_pk) if appointment_pk else None
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.pet = pet
            record.appointment = appointment
            record.save()
            return redirect('pet_detail', pk=pet_pk)  # Redirect to pet detail regardless of how the record was created
        return render(request, 'clinic/medical_record_form.html', {'form': form, 'pet': pet, 'appointment': appointment})

class BookingHotelView(View):
    def get(self, request):
        return render (request, 'booking_hotel.html')
    
class ServiceView(View):
    def get(self, request):
        return render (request, 'service.html')
    
class ServiceView(View):
    def get(self, request):
        return render (request, 'service.html')
    
class ShoppingView(View):
    def get(self, request):
        return render (request, 'shopping.html')
    
class ShoppingSweetView(View):
    def get(self, request):
        return render (request, 'shopping_sweet.html')
    
class ContactView(View):
    def get(self, request):
        return render (request, 'contact.html')