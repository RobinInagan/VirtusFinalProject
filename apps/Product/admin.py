from django.contrib import admin
from .models import *


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=["name","cost_per_unit","all_restaurants"]

class Products_RestaurantAdmin(admin.ModelAdmin):
    list_display=["product","restaurant"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Products_Restaurant,Products_RestaurantAdmin)