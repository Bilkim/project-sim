from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register, name='register'),
    path('login_user',views.login_user, name='login'),
    path('home', views.home, name='home'),
    path('forgot', views.forgot, name='forgot'),
]  