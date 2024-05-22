from django.shortcuts import render

# Other Modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
#Self Modules
from .models import *
from .serializers import *

class RestaurantViewSet(ModelViewSet):    
        queryset = Restaurant.objects.all()
        serializer_class = RestaurantSerializerModel

class TableViewSet(ModelViewSet):
        queryset = Table.objects.all()
        serializer_class = TablesSerializerModel

class Tables_RestaurantViewSet(ModelViewSet):
        queryset = Tables_Restaurant.objects.all()
        serializer_class = Tables_RestaurantSerializerModel

class OrderViewSet(ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializaerModel
