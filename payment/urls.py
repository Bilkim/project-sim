from django.urls import path
from . import views

urlpatterns = [
    path('payment/<packages_id>', views.payment, name='payment'),
    path('hotelPayment/<hotel_id>', views.hotelPayment, name='hotelPayment')
    
]