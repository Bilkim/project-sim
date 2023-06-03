from django.db import models
from vacations.models import MemberUsers
from django.conf import settings
from accounts.models import TourUser

# Create your models here.

class SpecialRooms(models.Model):
    hotelName = models.CharField('Hotel Name',max_length=300)
    roomImage = models.ImageField('Image', upload_to='Images/', default='img1.jpg')
    address = models.CharField('Location',max_length=50)
    phone = models.CharField('Contact Phone', max_length=50)
    description = models.TextField(blank=True)
    price = models.FloatField('Price per Night', max_length=150)
    

    def __str__(self):
        return self.hotelName
    

class HotelMembers(models.Model):
    last_name = models.OneToOneField(TourUser, null=True ,on_delete=models.CASCADE)
    inDate = models.DateField('Check In Date',max_length=50)
    outDate = models.DateField('Check Out Date', max_length=50)
    adultNo = models.IntegerField('Number of Adults')
    childrenNo = models.IntegerField('Number of Children')
    roomNo = models.IntegerField('Number of Rooms')
    

    def __str__(self):
        return str(self.last_name) 
    
