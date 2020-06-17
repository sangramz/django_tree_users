from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reseller, Customer
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
    """
    DESC : Main Page after the Login

    CONTEXT : Reseller & Customer Objects for Menu is being passed

    YET TO BE DONE:
    TARGET : Reseller = request.user.reseller ; To retrieve Reseller Model having only logged in user Attributes 
    Conclusion : Presently not working, Browse through all documentation as well SO, will find out ASAP

    """
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    context = { 'resellers' : resellers, 'customers' : customers }
    return render(request, 'main/dashboard/index.html', context)

"""
************************ RESELLER ACTIONS STARTS ************************

DESC: All the actions related to Reseller to be defined here. 
ACTIONS(So far) : Create, Update, Delete
"""
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
def ViewReseller(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    reseller_details = Reseller.objects.get(id=pk)
    context = { 'resellers' : resellers, 'customers' : customers, 'reseller_details' : reseller_details }
    return render(request, 'main/dashboard/view_reseller.html', context)


@login_required(login_url='login')
def EditReseller(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    reseller_details = Reseller.objects.get(id=pk)
    form = ResellerForm(instance=reseller_details)
    context = { 'resellers' : resellers, 
                'customers' : customers, 
                'reseller_details' : reseller_details,
                'form' : form }
    if request.method == 'POST':
        form = ResellerForm(request.POST, instance=reseller_details)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    return render(request, 'main/dashboard/create_reseller.html', context)

@login_required(login_url='login')
def DeleteReseller(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    reseller_details = Reseller.objects.get(id=pk)
    if request.method == 'POST':
        reseller_details.delete()
        return redirect('/dashboard/')
    context = { 'resellers' : resellers, 'customers' : customers, 'reseller_details' : reseller_details }
    return render(request, 'main/dashboard/view_reseller.html', context)

"""
************************ RESELLER ACTIONS ENDS ************************
"""


"""
************************ CUSTOMER ACTIONS STARTS ************************

DESC: All the actions related to be CUSTOMER to be defined here. 
ACTIONS(So far) : Create, Update, Delete
"""
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
def ViewCustomer(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    customer_details = Customer.objects.get(id=pk)
    context = { 'resellers' : resellers, 'customers' : customers, 'customer_details' : customer_details }
    return render(request, 'main/dashboard/view_customer.html', context)


@login_required(login_url='login')
def EditCustomer(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    customer_details = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer_details)
    context = { 'resellers' : resellers, 
                'customers' : customers, 
                'customer_details' : customer_details,
                'form' : form }
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer_details)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    return render(request, 'main/dashboard/create_customer.html', context)


@login_required(login_url='login')
def DeleteCustomer(request, pk):
    resellers = Reseller.objects.all()
    customers = Customer.objects.all()
    customer_details = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer_details.delete()
        return redirect('/dashboard/')
    context = { 'resellers' : resellers, 'customers' : customers, 'reseller_details' : reseller_details }
    return render(request, 'main/dashboard/view_reseller.html', context)

"""
************************ CUSTOMER ACTIONS ENDS ************************
"""