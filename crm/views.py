from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'crm/index.html')


def login_user(request):
    pass


def logout_user(request):
    pass


def register_user(request):
    pass

