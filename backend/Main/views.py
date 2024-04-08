from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
def showProducts(request):
                            #the location of html file
    return render(request, 'ViewProducts.html') #place 3rd argument if necessary

#admin auth website
def authLogin(request): #login the admin
    if request.user.is_authenticated: #will ask if the user is authenticated before redirecting to the site
        return redirect('authdashboard')
         
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('authdashboard')
        else:
            error_message = "Invalid username or password."
            return render(request, 'auth/login.html', {'error_message': error_message})
    else:
        return render(request, 'auth/login.html')

@login_required(login_url='authlogin')
def authDashboard(request):
    bch_vendo = VendoRegistration.objects.all()
    return render(request, 'auth/dashboard.html', {'user': request.user, 'bch_vendo':bch_vendo})

@login_required(login_url='authlogin')
def authInventories(request):
    return render(request, 'auth/inventories.html', {'user': request.user})

@login_required(login_url='authlogin')
def authNotifications(request):
    return render(request, 'auth/notifications.html', {'user': request.user})

@login_required(login_url='authlogin')
def authSales(request):
    return render(request, 'auth/sales_analysis.html', {'user': request.user})
    
def authTransactions(request):
    return render(request, 'auth/transactions.html', {'user': request.user})

@login_required(login_url='authlogin')
def authVendos(request):
    return render(request, 'auth/vendo_machines.html', {'user': request.user})

def addProduct(request):
        #Will post details and store database upon request
        product_count = int(request.POST.get('products_count'))

        #create a loop for multiple product details forms
        # for i in range(1, product_count + 1): #base loop

        if request.method =='POST':
            if request.POST.get('create_product_item'):
                product_form = ProductForm(request.POST, request.FILES)
                if product_form.is_valid():
                    product_form.save()
                    messages.success(request, 'Product added successfully')
                    return redirect('authdashboard')
                else:
                    error_message = product_form.errors
                    messages.success(request, error_message)
                    return redirect('authdashboard')
        else:
            product_form = ProductForm()
            return redirect('authdashboard')
        
        return render(request, 'auth/dashboard.html')

def registerVendo(request):
    #will register a vendo machine via serial number of the raspberry pi board
    if request.method == 'POST':
        if request.POST.get('register_vendo'):
            vendo_form = VendoRegForm(request.POST)
            if vendo_form.is_valid():
                vendo_form.save()
                messages.success(request, "Vendo successfully Registered")
                return redirect('authdashboard')
    
    return render(request, 'auth/dashboard.html')

    
