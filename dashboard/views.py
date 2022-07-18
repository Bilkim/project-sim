from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from dashboard.models import Order
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib import messages
from hotels.forms import HotelMemberForm, RoomForm
from vacations.forms import MemberForm, PackageForm
from vacations.models import Packages
from accounts.forms import createUserForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import  allowed_users, admin_only
from django.db.models import Sum
from time import gmtime, strftime

@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    users = User.objects.all()
    packageList = Packages.objects.all()
    bookingValue = Packages.objects.aggregate(Sum('latestPrice'))['latestPrice__sum']
    cust = User.objects.filter(username__isnull=False).count()
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    return render(request, 'dashboard.html', {'users': users, 'packageList':packageList, 'bookingValue': bookingValue, 'cust': cust, 'date': date})



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def transaction(request):
    return render(request, 'transactions.html', {})

@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def settings(request):
    userDet = User.objects.all()
    submitted = False
    if request.method == "POST":
        memberList = MemberForm(request.POST, request.FILES)
        if memberList.is_valid():
            memberList.save()
            return HttpResponseRedirect('settings?submitted=True')
    else:
        memberList = MemberForm
        if 'submitted' in request.GET:
            submitted = True

    memberList = MemberForm
    
    submitPackage = False
    if request.method == "POST":
        packFormList = PackageForm(request.POST, request.FILES)
        if packFormList.is_valid():
            packFormList.save()
            return HttpResponseRedirect('settings?submitPackage=True')
    else:
        packFormList = PackageForm
        if 'submitPackage' in request.GET:
            submitPackage = True

    packFormList = PackageForm
    
    submit = False
    if request.method == "POST":
        roomList = RoomForm(request.POST, request.FILES)
        if roomList.is_valid():
            roomList.save()
            return HttpResponseRedirect('settings?submit=True')
    else:
        roomList = RoomForm
        if 'submit' in request.GET:
            submit = True

    roomList = RoomForm
    
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()           
            
            messages.success(request, ("Registration Successful"))
            return redirect('dashboard')

    else: 
        form = createUserForm()

    
    return render(request, 'settings.html', {'memberList': memberList, 'packFormList': packFormList, 'submitPackage' : submitPackage, 'submitted': submitted, 'roomList': roomList, 'submit': submit, 'userDet': userDet, 'form': form})

@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def tables(request):
    return render(request, 'tables-bootstrap-tables.html', {})


def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('dashboard')

def deletePackage(request, package_id):
    package = Packages.objects.get(pk=package_id)
    package.delete()
    return redirect('dashboard')



