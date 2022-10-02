from email import message
from django.contrib.auth import authenticate,login, get_user_model
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.
from .models import *
from .forms import  createUserForm

User = get_user_model()


def home(request):
    return render(request, 'home.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           # Redirect to a success page.
           return redirect('booking')
        else:
           # Return an 'invalid login' error message.
           messages.error(request, ("Wrong password or email. Try Again!"))
           return redirect('login')

    else:
        return render(request, 'login.html');
    
    

    
    


def register(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
           # Redirect to a success page.            
            
            messages.success(request, ("Registration Successful"))
            return redirect('login')
        
        messages.error(request, "Unsuccessful registration. Invalid information.")

    else: 
        form = createUserForm()
      
    context = {'form': form}
    return render(request, 'register.html', context);

def forgot(request):
    
    context = {}
    return render(request, 'page-forgot-password.html', context)