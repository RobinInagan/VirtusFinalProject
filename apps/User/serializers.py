from rest_framework import serializers
from .models import *

class UserSeralizerModel(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id',"username","firstName","lastName","email","password"]

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        user = Users(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
    
class WaiterSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ['id',"user","charge"]

class WaiterShiftSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Waiter_Shift
        fields = "__all__"