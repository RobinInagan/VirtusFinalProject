from django.shortcuts import render

# Other Modules
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

#Self Modules
from .models import *
from .serializers import *


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSeralizerModel


class WaiterViewSet(ModelViewSet):
        queryset = Waiter.objects.all()
        serializer_class = WaiterSerializerModel

        permission_classes=[
             IsAuthenticated
        ]

        @action(detail=True, methods=['post'])
        def add_shift(self, request, pk=None):
            waiter = self.get_object()
            request.data['waiter']=waiter.id
            serializer = WaiterShiftSerializerModel(data=request.data)            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WaiterShiftViewSet(ModelViewSet):
      queryset = Waiter_Shift.objects.all()
      serializer_class = WaiterShiftSerializerModel
