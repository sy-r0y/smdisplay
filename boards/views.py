from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# What should the user see when they navigate to a certain page

# define your VIEW FUNCTIONs

# all VIEW FUNCTION take in the parameter 'request' ie HttpRequest that is passed to this view function


def index(request):
    return render(request, 'home.html')

def product_detail(request):
    return render(request, 'productdetail.html')

def add_to_cart(request):
    return render(request, 'addtocart.html')

def buy_now(request):
    return render(request, 'buynow.html')

def checkout(request):
    return render(request, 'checkout.html')

def profile(request):
    return render(request, 'profile.html')

def address(request):
    return render(request, 'address.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'customerregistration.html')

def change_password(request):
    return render(request, 'changepassword.html')

def orders(request):
    return render(request, 'orders.html')

def mobile(request):
    return render(request, 'mobile.html')