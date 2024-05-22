from django.db import models

# Imports From self Modules
from apps.User.models import Users,Waiter


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(Users,on_delete = models.DO_NOTHING)

    def __str__(self) ->str:
        return self.name
    

class Table(models.Model):
    number = models.IntegerField()
    personCapacity = models.IntegerField()

    def __str__(self) ->str:
        return str('Table Number = '+ str(self.number))

class Tables_Restaurant(models.Model):
    table = models.ForeignKey(Table,on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str('Table Number: '+str(self.table.number)+' Restaurant: '+str(self.restaurant.name))

class Order(models.Model):
    waiter = models.ForeignKey(Waiter,on_delete=models.DO_NOTHING)
    table_restaurant = models.ForeignKey(Tables_Restaurant,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.id)

class Products_Order(models.Model):
    product = models.ForeignKey('Product.Product',on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)

class Bill(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    cost = models.FloatField()
    tip_percent = models.DecimalField(max_digits=2, decimal_places=2)
    final_cost = models.FloatField()

    def __str__(self) -> str:
        return str('Order N° ='+str(self.id))