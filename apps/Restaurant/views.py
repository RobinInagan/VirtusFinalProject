from django.shortcuts import render

# Other Modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
import pytz
#Self Modules
from .models import *
from .serializers import *
from apps.User.models import Waiter_Shift,Waiter
from .permissions import isMG,isMG_AT

class RestaurantViewSet(ModelViewSet):    
        queryset = Restaurant.objects.all()
        serializer_class = RestaurantSerializerModel

class TableViewSet(ModelViewSet):
        queryset = Table.objects.all()
        serializer_class = TablesSerializerModel

class Tables_RestaurantViewSet(ModelViewSet):
        queryset = Tables_Restaurant.objects.all()
        serializer_class = Tables_RestaurantSerializerModel

        permission_classes = [
                        IsAuthenticated
                ]

        def list(self, request):
                col_tz = pytz.timezone('America/Bogota')
                now = datetime.now(col_tz)
                formatted_now = datetime.strptime(now.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                try:                        
                        waiter = Waiter.objects.get(user=request.user)
                        serializer = self.get_serializer(self.queryset, many=True)
                        shift = Waiter_Shift.objects.get(waiter=waiter.id)  
                        start_date = datetime.strptime(str(shift.start_date).split('+')[0],'%Y-%m-%d %H:%M:%S')
                        end_date = datetime.strptime(str(shift.end_date).split('+')[0],'%Y-%m-%d %H:%M:%S')

                        if start_date > formatted_now:
                                return Response({'error': 'Su jornada aún no comienza'},status=status.HTTP_400_BAD_REQUEST)
                        elif formatted_now > end_date:
                                return Response({'error': 'Su jornada ya finalizo'},status=status.HTTP_400_BAD_REQUEST)
                                                     
                        tables = Tables_Restaurant.objects.filter(restaurant=shift.restaurant)
                        serializer = self.get_serializer(tables, many=True)
                        return Response(serializer.data)
                                                               
                except Waiter.DoesNotExist:
                        return Response({'error': 'No hay un mesero asociado a el usuario que realiza la petición'},status=status.HTTP_400_BAD_REQUEST)
                except Waiter_Shift.DoesNotExist:
                        return Response({'error': 'No existe un horario definido para el mesero'},status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializaerModel

        permission_classes = [IsAuthenticated]

        def destroy(self, request, pk=None):
                self.permission_classes += [isMG_AT]
                self.check_permissions(request)

                order = self.get_object()
                order.delete()
                return Response({'Exito': 'Orden eliminada de manera exitosa'},status=status.HTTP_204_NO_CONTENT)

                                

class ProductsOrderViewSet(ModelViewSet):
        queryset = Products_Order.objects.all()
        serializer_class = ProductsOrderSerializerModel

class BillViewSet(ModelViewSet):
        queryset = Bill.objects.all()
        serializer_class = BillsSerializerModel

        permission_classes = [IsAuthenticated]

        def destroy(self, request, pk=None):
                self.permission_classes += [isMG]
                self.check_permissions(request)
                
                bill = self.get_object()
                bill.delete()
                return Response({'Exito': 'Cuenta eliminada de manera exitosa'},status=status.HTTP_204_NO_CONTENT)
                        

class TipWaiterViewSet(ModelViewSet):
        queryset = Tip_Waiter.objects.all()
        serializer_class = TipWaiterSerializerModel