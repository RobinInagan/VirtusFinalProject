from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'restaurants',RestaurantViewSet,basename='restaurants')
router.register(r'tables',TableViewSet,basename='tables')
router.register(r'tables_Restaurant',Tables_RestaurantViewSet,basename='tables_Restaurant')

urlpatterns = [
]

urlpatterns += router.urls