from django.db import models
from accounts.models import TourUser
from vacations.models import Packages
from hotels.models import SpecialRooms

# Create your models here.

class Package_Payment_Details(models.Model):   
    customer = models.ForeignKey(TourUser, on_delete=models.DO_NOTHING)
    package = models.ForeignKey(Packages, on_delete=models.DO_NOTHING)
    amount_paid = models.FloatField()
    no_of_attendees = models.PositiveIntegerField('Members Attending', default=1)
    


    def __str__(self):
        return str("Email: " + self.customer.email)
    
    
class Hotel_Payment_Details(models.Model):   
    customer = models.ForeignKey(TourUser, on_delete=models.DO_NOTHING)
    hotel = models.ForeignKey(SpecialRooms, on_delete=models.DO_NOTHING)
    amount_paid = models.FloatField()
    no_of_adults = models.PositiveIntegerField('Adults', default=1)
    no_of_children = models.PositiveIntegerField('Children', default=0)
    


    def __str__(self):
        return str("Email: " + self.customer.email)