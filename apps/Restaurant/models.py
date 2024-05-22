from django.db import models

# Imports From self Modules
from apps.User.models import Users


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


