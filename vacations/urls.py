from django.urls import path
from . import views

urlpatterns = [
    path('booking',views.booking, name='booking'),
    path('events',views.events, name = 'events'),
    path('index',views.index, name='index'),
    path('hotelBook',views.hotelBook, name='hotelBook'),
    path('logout',views.logout_user, name='logout'),
    path('venue',views.venue, name='venue'),
    path('show_venue/<book_id>', views.show_venue, name='show-venue' ),
    path('packages/<packages_id>',views.packages, name='packages'),
]  