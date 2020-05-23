from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('CreateReseller/', views.CreateReseller, name='CreateReseller'),
    path('CreateCustomer/', views.CreateCustomer, name='CreateCustomer'),
]