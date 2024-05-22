from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["name","address","owner"]
    
class TableAdmin(admin.ModelAdmin):
    list_display =["number","personCapacity"]

class Tables_RestaurantAdmin(admin.ModelAdmin):
    list_display =["table","restaurant"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["waiter","table_restaurant"]

class ProductsOrderAdmin(admin.ModelAdmin):
    list_display = ["product","order"]

class BillAdmin(admin.ModelAdmin):
    list_display = ["id","order","cost","tip_percent","final_cost"]

class TipWaiterAdmin(admin.ModelAdmin):
    list_display = ["id","bill","waiter","paid"]


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Tables_Restaurant,Tables_RestaurantAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Products_Order,ProductsOrderAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Tip_Waiter,TipWaiterAdmin)
