# models.py module used to define classes or new types for modelling the concept of this app 'board'

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# board size, board fabric, board type

BOARD_CHOICES=(
    ('magnetic','MagnetiC Board'), ('nonmagnetic','Non-Magnetic'),
    ('marker','Marker Board'), ('pinup','Soft Board'),
    ('easel','Easel Board'), ('glass','Glass Board')
) 
CATEGORY_CHOICES=(
    ('magnetic','Magnetic'), ('nonmagnetic','Non-Magnetic'),
    ('pinup','Soft Board'), ('marker','Marker Board'),
    ('mdf', 'MDF Board')
)

STATUS_CHOICES= (
    ('a','accepted'), ('p','packed'), 
    ('otw','on the way'), ('d','delivered'), 
    ('c','cancel')
)

class Customer(models.Model):
    # Customer model would have many-to-one relation with User
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city= models.CharField(max_length=50)
    zipcode= models.IntegerField()
    boards= models.CharField(choices=BOARD_CHOICES, max_length=50)
    def __str__(self):
        return str(self.id)


class Product(models.Model):
    title= models.CharField(max_length=100)
    selling_price= models.FloatField()
    discount_price= models.FloatField()
    description= models.TextField()
    brand= models.CharField(max_length=100)
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_image= models.ImageField(upload_to= 'productimg')
    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    ordered_date= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

