from rest_framework import serializers
from .models import *

class UserSeralizerModel(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'FirstName', 'SecondName']

class WaiterSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = "__all__"

class WaiterShiftSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Waiter_Shift
        fields = "__all__"