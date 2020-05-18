from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def dashboard(request):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    context = { 'resellers' : resellers, 'customers' : customers }
    return render(request, 'main/dashboard/index.html', context)

def login(request):
    return render(request, 'main/login/login.html')
