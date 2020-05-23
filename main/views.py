from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from . forms import ResellerForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'main/login/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    context = { 'resellers' : resellers, 'customers' : customers }
    return render(request, 'main/dashboard/index.html', context)

@login_required(login_url='login')
def CreateReseller(request):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    form = ResellerForm()
    if request.method == 'POST':
        form = ResellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/') 
    context = { 'resellers' : resellers, 'customers' : customers, 'form' : form }
    return render(request, 'main/dashboard/create_reseller.html', context)

@login_required(login_url='login')
def CreateCustomer(request):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/') 
    context = { 'resellers' : resellers, 'customers' : customers, 'form' : form }
    return render(request, 'main/dashboard/create_customer.html', context)

@login_required(login_url='login')
def ViewReseller(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    reseller_details = Reseller.objects.get(id=pk)
    context = { 'resellers' : resellers, 'customers' : customers, 'reseller_details' : reseller_details }
    return render(request, 'main/dashboard/view_reseller.html', context)

@login_required(login_url='login')
def ViewCustomer(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    customer_details = Customer.objects.get(id=pk)
    context = { 'resellers' : resellers, 'customers' : customers, 'customer_details' : customer_details }
    return render(request, 'main/dashboard/view_customer.html', context)
