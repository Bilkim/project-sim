from django import forms
from django.forms import ModelForm, widgets
from .models import Book, MemberUsers, Packages
from accounts.models import TourUser


#Creating the book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name','image','address','phone','arrDate','leavDate')
        labels = {
            'name': '',
            'image': '',
            'address': '',
            'phone': '',
            'arrDate': 'Start Date',
            'leavDate': 'End Date',


        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contact'}),
            'arrDate': forms.DateInput(attrs={'class':'form-control ', 'placeholder': 'Start Date', 'type': 'Date'}),
            'leavDate': forms.DateInput(attrs={'class':'form-control ', 'placeholder': 'End Date', 'type': 'Date'}),

            
        }
        
        
class PackageForm(ModelForm):
    class Meta:
        model = Packages
        fields = ('city','name','image','address','phone','arrDate','leavDate','description1','description2','description3','prevPrice','latestPrice')
        labels = {
            'city': '',
            'name': '',
            'image': '',
            'address': '',
            'phone': '',
            'arrDate': 'Start Date',
            'leavDate': 'End Date',
            'description1': 'description1',
            'description2': 'description2',
            'description3': 'description3',
            'prevPrice': 'Previous Price',
            'latestPrice': 'Latest Offer',


        }

        widgets = {
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contact'}),
            'arrDate': forms.DateInput(attrs={'class':'form-control ', 'placeholder': 'Start Date', 'type': 'Date'}),
            'leavDate': forms.DateInput(attrs={'class':'form-control ', 'placeholder': 'End Date', 'type': 'Date'}),
            'description1': forms.TextInput(attrs={'class':'form-control ', 'type': 'text'}),
            'description2': forms.TextInput(attrs={'class':'form-control '}),
            'description3': forms.TextInput(attrs={'class':'form-control '}),
            'prevPrice': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Previous Price'}),
            'latestPrice': forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Latest Offer'}),

            
        }


class MemberForm(ModelForm):
    class Meta:
        model = MemberUsers
        fields = ('address', 'phone','city','email', 'members', )
        labels = {
            'address': '',
            'phone': '',
            'city': '',
            'email':'',
            'members': '',


        }

        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Personl Address', 'id': 'address'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone number', 'id': 'phone'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'City', 'id': 'city'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address', 'type': 'email', 'id': 'email'}),
            'members': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Family/Friends attending', 'type': 'number', 'id': 'birthday'}),
        }