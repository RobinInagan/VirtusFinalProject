from django.shortcuts import render

# Other Modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
#Self Modules
from .models import *
from .serializers import *


class ProductViewSet(ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProdcutsSerializerModel

class Products_RestaurantViewSet(ModelViewSet):
        queryset = Products_Restaurant.objects.all()
        serializer_class = Products_RestaurantSerializerModel