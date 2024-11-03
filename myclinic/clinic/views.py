from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  # For class-based views
from django.views import View # Base class for class-based views
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib import messages

class HomeView(View):  # Class-based view for the home page
    def get(self, request):
        return render(request, 'home.html')


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
        form = BookingForm()
        return render(request, 'booking_hotel.html', {'form': form})
    
    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel')
        return render(request, 'booking_hotel.html', {'form': form})
    
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
    
class ReservView(View):
    def get(self, request):
        form = ReservForm()
        return render(request, 'reservation.html', {'form': form})
    
    def post(self, request):
        form = ReservForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel')
        return render(request, 'reservation.html', {'form': form})
    
class RegisterView(View):
    def get(self, request):
        form = CreateUser()
        return render(request, "register.html", {
            "form" : form
        })
    
    def post(self, request):
        form = CreateUser(request.POST)

        if form.is_valid():
            user = form.save()
            print(request.POST)

            User.objects.create(
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email,
                authen = user
            ) 

            messages.success(request, 'Account was create for ' + user.username)
            return redirect('login')
        else:
            messages.success(request, 'กรุณาตรวจสอบแบบฟอร์มให้ละเอียด')
            return render(request, "register.html", {
                "form": form
            })


class LoginView(View):
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request,user)

        return render(request,'login.html', {"form":form})

