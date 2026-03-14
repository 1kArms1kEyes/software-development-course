from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "products"

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'colors', ColorViewSet, basename='color')
router.register(r'networks', MaxSupportNetworkViewSet, basename='network')
router.register(r'operating-systems', OperatingSystemViewSet, basename='operating-system')
router.register(r'', ProductViewSet, basename='products')

urlpatterns = [
    path("filters/", ProductFilterOptionsView.as_view(), name="product-filters"),
    path('', include(router.urls)),
]
