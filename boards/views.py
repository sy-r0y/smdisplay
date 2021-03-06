from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# Create your views here.
# FUNCTION BASED VIEW OR CLASS BASED VIEW
# What should the user see when they navigate to a certain page

# define your VIEW FUNCTIONS or VIEW CLASSES

# all VIEW FUNCTION take in the parameter 'request' ie HttpRequest that is passed to this view function


# def index(request):
#    return render(request, 'home.html')

class BoardHomeView(View):  # inherits the View class
    def get(self, request):
        magnetic = Product.objects.filter(category='magnetic')
        nonmagnetic = Product.objects.filter(category='nonmagnetic')
        marker = Product.objects.filter(category='marker')
        pinup = Product.objects.filter(category='pinup')
        mdf = Product.objects.filter(category='mdf')
        return render(request, 'home.html', {'magnetic': magnetic, 'nonmagnetic': nonmagnetic,
                                                     'marker': marker, 'pinup': pinup,
                                                     'mdf': mdf}
                     )
class ProductDetailView(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        # print(product.id)
        return render(request, 'productdetail.html', {'product':product})

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

class MobileView(View):
    def get(self, request, category=None):
        #mobiles=[]
        if category==None:
            mobiles=Product.objects.filter(category='magnetic')
        elif category== 'magnetic' or category=='nonmagnetic' or category=='pinup' or category=='mdf':
            mobiles=Product.objects.filter(category=category)
        elif category=='below':
            mobiles=Product.objects.filter(discount_price__lt=3000)
        elif category=='above':
            mobiles=Product.objects.filter(discount_price__gt=3000)
                
        return render(request, 'mobile.html', {'mobiles':mobiles})