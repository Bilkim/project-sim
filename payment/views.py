from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import TourUser
from vacations.models import MemberUsers, Packages
from vacations.forms import PackageForm
from django.contrib.auth import get_user_model
from hotels.models import SpecialRooms, HotelMembers
from hotels.forms import RoomForm
from hotels.models import HotelMembers, SpecialRooms
from hotels.forms import UserFilter

User = get_user_model()

# Create your views here.

def payment(request, packages_id):
    package = Packages.objects.get(pk=packages_id)
    price = package.latestPrice 
    
    user = TourUser.objects.get(email = request.user.email)
    print(user.email)
    
    arr_date = package.arrDate
    leave_date = package.leavDate
    
    duration = (leave_date - arr_date).days
    
    members_list = MemberUsers.objects.get(first_name = user)    
    
    all_members = MemberUsers.objects.all()   
    memb_filter = UserFilter(request.GET, queryset = all_members)  
    
    
    attendees = members_list.members    
    totalPrice = price * attendees
    dollarPrice = totalPrice/100 
    
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
       dis =  PackageForm(request.POST or None)
       if dis.is_valid():
           instance = dis.save(commit=False)
           instance.user = request.user
           instance.save()
       return redirect('payment:payment')
    else:
        instance= PackageForm
        
    context={'instance':instance}     
    

    
    return render (request, 'paymbase.html',
           {'package': package, 'user': user, 'duration': duration,'context' : context, 'filter': memb_filter, 'att': attendees,'price': totalPrice, 'price2': dollarPrice})


def hotelPayment(request, hotel_id):
    hotel = SpecialRooms.objects.get(pk=hotel_id)
    price = hotel.price  
    
    users = request.user
    
    hotel_list = HotelMembers.objects.all()
    hotel_filter = UserFilter(request.GET, queryset = hotel_list)    
    member = HotelMembers.objects.get(last_name = users)  
    
    adult = member.adultNo
    children = member.childrenNo     
    
    in_date = member.inDate
    out_date = member.outDate
    days = (out_date - in_date).days
    

    totalFamily = adult + children
    totalPrice = price * totalFamily * days    
    dollarPrice = totalPrice/100
    
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
       dis =  RoomForm(request.POST or None)
       if dis.is_valid():
           instance = dis.save(commit=False)
           instance.user = request.user
           instance.save()
       return redirect('payment:payment')
    else:
        instance= RoomForm
        
    context={'instance':instance}  
    

    
    return render (request, 'hotelPayment.html',
           {'hotels': hotel,'hotelList': hotel_list, 'total_days': days, 'member_details': member,'user': users,'family': totalFamily, 'hotelFilter': hotel_filter ,'roomPrice': price, 'totalPrice': totalPrice, 'roomPrice2': dollarPrice, 'context':context})


def pay(request):
    return render(request, 'options_base.html');