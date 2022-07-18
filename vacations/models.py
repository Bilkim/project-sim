from django.db import models
from accounts.models import TourUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

# Create your models here.

class Book(models.Model):
    name = models.CharField('Vacation Name',max_length=150)
    image = models.ImageField('Image', upload_to='Images/', default='default.jpg')
    address = models.CharField('Venue Address',max_length=300)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    arrDate = models.DateField('Start Date',max_length=50, auto_now_add=False, auto_now=False, blank=True)
    leavDate = models.DateField('End Date ',max_length=50, auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.name
    
class Packages(models.Model):
    city = models.CharField('City Name',max_length=150)
    name = models.CharField('Vacation Name',max_length=150)
    image = models.ImageField('Image', upload_to='Images/', default='default.jpg')
    address = models.CharField('Venue Address',max_length=300)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    arrDate = models.DateField('Start Date',max_length=50, auto_now_add=False, auto_now=False, blank=True)
    leavDate = models.DateField('End Date ',max_length=50, auto_now_add=False, auto_now=False, blank=True)
    description1 = models.TextField('Package description 1',blank=True)
    description2 = models.TextField('Package description 2',blank=True)
    description3 = models.TextField('Package description 3',blank=True)
    prevPrice = models.FloatField('Previous Price', max_length=150)
    latestPrice = models.FloatField('Latest Offer Price', max_length=150)

    def __str__(self):
        return self.name

class MemberUsers(models.Model):   
    first_name = models.OneToOneField(TourUser, on_delete=models.DO_NOTHING)
    address = models.CharField('Member Address',max_length=300, blank=True)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    city = models.CharField('City', max_length=150, blank=True)
    email = models.EmailField('Email ', max_length=150, blank=True)
    members = models.PositiveIntegerField('Members Attending', default=1)
    


    def __str__(self):
        return str(self.phone)


class Event(models.Model):
    name = models.CharField('Venue Name',max_length=150, default='Not Added Yet')
    vacationDate = models.DateTimeField('Vacation Date',max_length=150, null=True)
    venue = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    web = models.URLField('Website Address', max_length=50,null=True, blank=True)
    #venue = models.CharField(max_length=150)
    manager = models.ForeignKey(TourUser , null=True, on_delete=models.SET_NULL)
    email = models.EmailField('Email Address', max_length=50, blank=True)
    description = models.TextField(null=True,blank=True)
    attendees = models.ManyToManyField(MemberUsers, blank=True)

    def __str__(self):
        return self.name
    
    

