from django.contrib import admin
from django.urls import path
from .views import ProductInfo, LatestArrivals

urlpatterns = [
    path('product/<int:product_id>/', ProductInfo.as_view(), name='Single product information'),
    path('latest_arrivals/', LatestArrivals.as_view(), name='Latest arrivals'),
]   