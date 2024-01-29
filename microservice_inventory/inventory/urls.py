from django.contrib import admin
from django.urls import path
from .views import ProductInfo

urlpatterns = [
    path('product/<int:product_id>/', ProductInfo.as_view(), name='Single product information'),
]   