from django.shortcuts import render

# Other Modules
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#Self Modules
from .models import *
from .serializers import *
from apps.Restaurant.models import Order
from apps.Restaurant.serializers import OrderSerializaerModel


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSeralizerModel


class WaiterViewSet(ModelViewSet):
        queryset = Waiter.objects.all()
        serializer_class = WaiterSerializerModel

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
            
        def get_serializer_class(self):
             print(self.request.query_params)
             return super().get_serializer_class()
        
        @action(detail=True, methods=['get'])
        def orders(self, request, pk=None):
            waiter = self.get_object()
            active = request.query_params.get('active')
            if active:
                orders = Order.objects.filter(waiter=waiter.id).filter(
                    models.Q(bill__isnull=True) | models.Q(bill__final_cost__isnull=True)
                )
            else:
                orders = Order.objects.filter(waiter=waiter.id)
            serializer = OrderSerializaerModel(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class WaiterShiftViewSet(ModelViewSet):
      queryset = Waiter_Shift.objects.all()
      serializer_class = WaiterShiftSerializerModel
