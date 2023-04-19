from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

# allow access to index page if user is logged in


@login_required(login_url='login')
def index(request):
    return render(request, 'crm/index.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Successfully Logged in!")
            return redirect('/')
        else:
            messages.error(request, "There was an error. Please try again...or signup!")
            return redirect('/')
    else:
        return render(request, 'crm/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Successfully Logged Out! See you next time ;)")
    return redirect('/login')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        try:
            validate_email(username)
            valid_email = True
        except validate_email.ValidationError:
            valid_email = False

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Successfully Logged in!")
            return redirect('/')
        else:
            messages.error(request, "There was an error. Please try again...or signup!")
            return redirect('/')
    else:
        return render(request, 'crm/signup.html')
