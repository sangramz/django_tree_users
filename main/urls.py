from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('CreateReseller/', views.CreateReseller, name='CreateReseller'),
    path('ViewReseller/<str:pk>', views.ViewReseller, name='ViewReseller'),
    path('CreateCustomer/', views.CreateCustomer, name='CreateCustomer'),
    path('ViewCustomer/<str:pk>', views.ViewCustomer, name='ViewCustomer'),
]