from rest_framework import serializers
from .models import *

class ProdcutsSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class Products_RestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Products_Restaurant
        fields = "__all__"    