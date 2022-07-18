from django import forms
from django.forms import ModelForm
from .models import SpecialRooms, HotelMembers
from django.contrib.auth.models import User
from django_filters import FilterSet

class RoomForm(ModelForm):
    class Meta:
        model = SpecialRooms
        fields = ('hotelName','roomImage','address','phone','description','price')
        labels = {
            'hotelName': '',
            'roomImage': '',
            'address': '',
            'phone': '',
            'description': '',
            'price': '',


        }

        widgets = {
            'hotelName': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Hotel Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Location Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Phone Number'}),
            'description': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Enter the room description'}),
            'price': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Price per Night'}),
            
        }
        

class HotelMemberForm(ModelForm):
    class Meta:
        model = HotelMembers
        fields = ('last_name','inDate','outDate','adultNo','childrenNo', 'roomNo')
        labels = {
            'last_name': '',
            'inDate': '',
            'outDate': '',
            'adultNo': '',
            'childrenNo': '',
            'roomNo': '',


        }

        widgets = {
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Guest Name'}),
            'inDate': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Check In Date', 'type': 'date', 'id': 'checkin-date'}),
            'outDate': forms.NumberInput(attrs={'class':'form-control ', 'placeholder': 'Check Out Date', 'type': 'date', 'id': 'checkout-date'}),
            'adultNo': forms.NumberInput(attrs={'class':'form-control ', 'placeholder': 'Number of adults(above 18 years old)', 'type': 'number', 'id': 'adult'}),
            'childrenNo': forms.NumberInput(attrs={'class':'form-control ', 'placeholder': 'Number of children( below 18 years old)', 'type': 'number', 'id': 'children'}),
            'roomNo': forms.NumberInput(attrs={'class':'form-control ', 'placeholder': 'Number of rooms)', 'type': 'number', 'id': 'rooms'}),
            
        }
        
class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = '__all__'



