from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    #URLs specific to Reseller
    path('CreateReseller/', views.CreateReseller, name='CreateReseller'),
    path('ViewReseller/<str:pk>', views.ViewReseller, name='ViewReseller'),
    path('EditReseller/<str:pk>', views.EditReseller, name='EditReseller'),
    path('DeleteReseller/<str:pk>', views.DeleteReseller, name='DeleteReseller'),

    #URLs specific to Reseller
    path('CreateCustomer/', views.CreateCustomer, name='CreateCustomer'),
    path('ViewCustomer/<str:pk>', views.ViewCustomer, name='ViewCustomer'),
    path('EditCustomer/<str:pk>', views.EditCustomer, name='EditCustomer'),
    path('DeleteCustomer/<str:pk>', views.DeleteCustomer, name='DeleteCustomer'),
]