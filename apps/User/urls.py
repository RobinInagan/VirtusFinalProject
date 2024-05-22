from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users',UsersViewSet,basename='users')
router.register(r'waiters',WaiterViewSet,basename='waiters')
router.register(r'waitershift',WaiterShiftViewSet,basename='waitershift')

urlpatterns = [
]

urlpatterns += router.urls