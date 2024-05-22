from django.shortcuts import render

# Other Modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
#Self Modules
from .models import *
from .serializers import *


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSeralizerModel


class WaiterViewSet(ModelViewSet):
        queryset = Waiter.objects.all()
        serializer_class = WaiterSerializerModel

class WaiterShiftViewSet(ModelViewSet):
      queryset = Waiter_Shift.objects.all()
      serializer_class = WaiterShiftSerializerModel
