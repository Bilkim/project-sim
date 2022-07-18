from django.db import models
from django.db.models.deletion import CASCADE
from vacations.models import Book, Packages, MemberUsers, Event
from hotels.models import SpecialRooms

    
class CustomerChoice(models.Model):
    customerName = models.ForeignKey(MemberUsers, on_delete=models.CASCADE)
    tourChoice = models.ForeignKey(Packages, on_delete=models.CASCADE)
    hotelChoice = models.ForeignKey(SpecialRooms,null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.customerName)
    


class Order(models.Model):
    tourOrder = models.ForeignKey(Packages, blank=True, null=True, on_delete=models.CASCADE)
    tourAmount = models.CharField('Amount per tour', blank=True, null=True,max_length=150)
    totalAmount = models.CharField('Total Amount', blank=True, null=True,max_length=150)
    
    def __str__(self):
        return self.tourOrder
    
