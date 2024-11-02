from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('booking-hotel/', views.BookingHotelView.as_view(), name='hotel'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('shopping/', views.ShoppingView.as_view(), name='shopping'),
    path('shopping/sweet/', views.ShoppingView.as_view(), name='shopping_sweet'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('reserv/', views.ReservView.as_view(), name='reserv'),
]