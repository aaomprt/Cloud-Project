from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  # For class-based views
from django.views import View # Base class for class-based views
from .models import *
from .forms import *



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
    
