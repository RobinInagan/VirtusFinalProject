from rest_framework import serializers
from .models import *

class RestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Restaurant
        fields="__all__"

class TablesSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields="__all__"

class Tables_RestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Tables_Restaurant
        fields = "__all__"

class OrderSerializaerModel(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ProductsOrderSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Products_Order
        fields = "__all__"

class BillsSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

class TipWaiterSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Tip_Waiter
        fields= "__all__"