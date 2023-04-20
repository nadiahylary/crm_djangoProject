from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from crm.forms import SignUpForm, AddCustomerForm
from crm.models import Customer


# Create your views here.

# allow access to index page if user is logged in


@login_required(login_url='login')
def index(request):
    return render(request, 'crm/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Successfully Logged in!")
            return redirect('index')
        else:
            messages.error(request, "There was an error. Please try again...or signup!")
            return redirect('index')
    else:
        return render(request, 'crm/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Successfully Logged Out! See you next time ;)")
    return redirect('/login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Auto authenticate the user:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your account was Successfully Created! Cheers!")
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'crm/signup.html', {'form': form})
    return render(request, 'crm/signup.html', {'form': form})


@login_required(login_url='login')
def customers_List(request):
    form = AddCustomerForm(request.POST or None)
    if request.method == 'POST':
        # get the data from the add new customer form
        # create a new user with that data
        # commit to the db
        # then redirect to index page
        if form.is_valid():
            form.save()
            messages.success(request, "New Customer Added Successfully...")
            return redirect('index')
    else:
        customers = Customer.objects.all().order_by('created_at')
        return render(request, 'crm/customers.html', {'customers': customers, 'form': form})


@login_required(login_url='login')
def edit_customer(request, pk):
    if request.method == 'POST':
        customer = Customer.objects.get(id=pk)
        # set customer's data to updated data from the form
        # save to db
        # then redirect to customers' page
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer's Details Has Been Updated!")
            return redirect('customers')
        return render(request, 'crm/edit-customer.html', {'form': form})
    else:
        customer = Customer.objects.get(id=pk)
        return render(request, 'crm/customer-detail.html', {'customer': customer})


# delete a customer from db
@login_required(login_url='login')
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    messages.success(request, "Customer Deleted Successfully.")
    return redirect('customers')
