from django.contrib import admin
from .models import Order, CustomerChoice

# Register your models here.
@admin.register(CustomerChoice)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'tourChoice', 'hotelChoice')
    ordering = ('tourChoice',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tourOrder', 'tourAmount', 'totalAmount')
    ordering = ('tourOrder',)
