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
    

class BookingHistoryView(View):
    def get(self, request):
        hotel_bookings = BookingHotel.objects.all()  # ดึงข้อมูลการจองจากโมเดล BookingHotel
        reservations = Reservation.objects.all()      # ดึงข้อมูลการจองจากโมเดล Reservation
        
        context = {
            'hotel_bookings': hotel_bookings,
            'reservations': reservations,
        }
        return render(request, 'booking_history.html', context)

