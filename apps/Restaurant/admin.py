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


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Tables_Restaurant,Tables_RestaurantAdmin)
admin.site.register(Order,OrderAdmin)
