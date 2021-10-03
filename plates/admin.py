from django.contrib import admin
from .models import Plates

# Register your models here.


class PlateAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'description', 'price',
        'plate_images', 'category'
    ]

admin.site.register(Plates, PlateAdmin)