# Register your MODELS here on admin.py

# admin module is used for defining how administrative panel would look like


from django.contrib import admin

from .models import Customer, Product, Cart, OrderPlaced

# Now in the admin.py module, we register our Models to be managed in the Adminsitrative panel
# By convention, Model name is joined with "Admin"


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'locality', 'city', 'zipcode', 'boards']
    
    # list_display is a pre-built attribute
    # list_display tells Django, which model attributes to display in the admin panel
    

class ProductAdmin(admin.ModelAdmin):
    list_displa = [
        'title','selling_price', 'discount_price', 'descriptions',
        'brand', 'category'
    ]


class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'product', 'quantity'
    ]


class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=[
        'user', 'product', 'quantity', 'ordered_date', 'status'
    ]


# NOW, we need to register the Model Admins created here with their corresponding Models
# This tells Django, which admins to associate with which models

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(OrderPlaced, OrderPlacedAdmin)