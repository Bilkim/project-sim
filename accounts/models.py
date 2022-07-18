from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class CustomAccountManager(BaseUserManager):


    def create_user(self, email, username, first_name,last_name, password, **other_fields):
            if not email:
                raise ValueError(gettext_lazy('You must provide an email address'))
            
            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_superuser', False)
            other_fields.setdefault('is_active', True)

            email = self.normalize_email(email)
            user = self.model(email=email, username=username, first_name=first_name,
                               last_name=last_name, **other_fields)
            
            user.set_password(password)
            user.save()
            return user
        
    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_superuser') is not True:
           raise ValueError(
                'Superuser must be assigned to is_superuser = True.')

        return self.create_user(email, username, first_name, last_name, password, **other_fields)



class TourUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'),unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)    
    phone_number = models.CharField( max_length=12, unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.username



