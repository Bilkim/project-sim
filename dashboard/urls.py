from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard',views.dashboard, name='dashboard'),  
    path('transaction',views.transaction, name='transaction'),
    path('settings',views.settings, name='settings'),
    path('tables',views.tables, name='tables'),   
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/<user_id>", views.delete, name="delete"),
    path("deletePackage/<package_id>", views.deletePackage, name="deletePackage")
]