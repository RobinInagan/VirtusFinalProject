from django.contrib import admin

# Register your models here.

from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display=['id',"username","firstName","lastName","email","password"]

class WaiterAdmin(admin.ModelAdmin):
    list_display =["user","charge"]

class WaiterShiftAdmin(admin.ModelAdmin):
    list_display=["waiter","start_date","end_date","restaurant"]

admin.site.register(Users,UsersAdmin)
admin.site.register(Waiter,WaiterAdmin)
admin.site.register(Waiter_Shift,WaiterShiftAdmin)