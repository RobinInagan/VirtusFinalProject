from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(r'products',ProductViewSet,basename='products')
router.register(r'products_restaurants',Products_RestaurantViewSet,basename='products_restaurants')


urlpatterns = [
]

urlpatterns += router.urls