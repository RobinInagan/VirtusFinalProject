from rest_framework.permissions import BasePermission
from apps.User.models import Waiter

class isMG(BasePermission):
    
    def has_permission(self, request, view):

        waiter = Waiter.objects.get(user=request.user)
        if waiter.charge == 'MG':
            return True
        else:
            return False
        

class isMG_AT(BasePermission):
    
    def has_permission(self, request, view):

        waiter=Waiter.objects.get(user=request.user)
        if waiter.charge == 'MG' or waiter.charge == 'AT':
            return True
        else:
            return False
