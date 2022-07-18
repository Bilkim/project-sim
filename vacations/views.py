from django.shortcuts import render
from .models import Event, Book, MemberUsers, Packages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from .forms import BookForm, MemberForm, PackageForm
from django.contrib.auth import get_user_model,logout
from hotels.forms import HotelMemberForm, RoomForm
from hotels.models import HotelMembers, SpecialRooms
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

User = get_user_model()


# Create your views here.
def show_venue(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'show_venue.html',
    {'book': book})

def venue(request):
    venue_list = Book.objects.all()
    return render(request, 'venue.html',
    {'venue_list': venue_list})
    
@login_required(login_url='login_user')
def booking(request):
    venueList = Book.objects.all()
    packageList = Packages.objects.all()
    member = MemberUsers.objects.filter(first_name = request.user).exists()

    submitted = False
    if request.method == "POST":
        if member:            
            member = MemberUsers.objects.get(first_name = request.user)
            memberList = MemberForm(request.POST, request.FILES, instance = member)            
            if memberList.is_valid():
                memberList.save()
                messages.success(request, ("User details updated successfully"))
                return HttpResponseRedirect('booking?submitted=True#book')
        else:
            memberList = MemberForm(request.POST, request.FILES)            
            if memberList.is_valid():
                memberList.instance.first_name = request.user
                memberList.save()
                messages.success(request, ("User details created successfully"))
                return HttpResponseRedirect('booking?submitted=True#book')
    else:
        memberList = MemberForm
        if 'submitted' in request.GET:
            submitted = True

    memberList = MemberForm 
        
        
    return render(request, 'booking.html',
    {'packageList': packageList, 'venueList': venueList, 'memberList': memberList, 'submitted': submitted})


def packages(request, packages_id):
    package = Packages.objects.get(pk=packages_id)

    submitPackage = False
    if request.method == "POST":
        packFormList = PackageForm(request.POST, request.FILES)
        if packFormList.is_valid():
            packFormList.save()
            return HttpResponseRedirect('booking?submitPackage=True')
    else:
        packFormList = PackageForm
        if 'submitPackage' in request.GET:
            submitPackage = True

    packFormList = PackageForm
        
    return render(request, 'packages.html',
    {'package': package, 'packFormList': packFormList, 'submitPackage': submitPackage})


def events(request):
    event_list = Event.objects.all()
    return render(request, 'events.html',
    {'event_list': event_list})

def index(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('index?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True

    form = BookForm
    return render(request, 'index.html', {'form': form, 'submitted': submitted})


def hotelBook(request):
    hotelMemberList = HotelMembers.objects.all()
    hotelRoom = SpecialRooms.objects.all()

    submit = False
    if request.method == "POST":
        membList = HotelMemberForm(request.POST, request.FILES)
        if membList.is_valid():
            membList.save()
            return HttpResponseRedirect('hotelBook?submit=True')
    else:
        membList = HotelMemberForm
        if 'submit' in request.GET:
            submit = True

    membList = HotelMemberForm
    return render(request, 'hotelBook.html',
    {'hotelMemberList': hotelMemberList, 'hotelRoom': hotelRoom, 'membList': membList, 'submit': submit})


def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'home.html')