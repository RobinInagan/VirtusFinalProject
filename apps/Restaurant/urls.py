from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'restaurants',RestaurantViewSet,basename='restaurants')
router.register(r'tables',TableViewSet,basename='tables')
router.register(r'tables_restaurant',Tables_RestaurantViewSet,basename='tables_restaurant')
router.register(r'orders',OrderViewSet,basename='orders')
router.register(r'products_order',ProductsOrderViewSet,basename='products_order')
router.register(r'bills',BillViewSet,basename='bills')

urlpatterns = [
]

urlpatterns += router.urls