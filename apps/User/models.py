from django.db import models

from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    REQUIRED_FIELDS = ["email","FirstName","SecondName"]
     
    FirstName = models.CharField(max_length=50,default="")
    SecondName = models.CharField(max_length=50,default="")
    email = models.EmailField(unique=True)

    def save(self, *args,**kwargs) -> None:
        self.username = self.email.split('@')[0]
        return super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.username
    
    
class Waiter(models.Model):
    chargeChoices = (('MG', 'MANAGER'), ('AT', 'ADMINTABLES'), ('EX', 'EXTRA'))
    user = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    charge = models.CharField(max_length=10,choices=chargeChoices)

    def __str__(self) -> str:
        return self.user.username

class Waiter_Shift(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    restaurant = models.ForeignKey('Restaurant.Restaurant', on_delete=models.DO_NOTHING,default="")