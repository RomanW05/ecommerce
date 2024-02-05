from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Products
# from .populate import populate_item
from .serializer import ProductSerializer

import logging

logger = logging.getLogger('main')
# populate_item()
# Create your views here.

class ProductInfo(generics.GenericAPIView):
    permission_class = (permissions.AllowAny,)
    authentication_classes = []
    serializer_class = ProductSerializer
    def get(self, request, product_id):
        product_info = Products.objects.filter(id=product_id).first()
        if product_info is None:
            return Response({'message': "Product not found"}, status=status.HTTP_400_NOT_FOUND)
        serialized_product = ProductSerializer(product_info)
        logger.debug(serialized_product)
        return Response({'message': "ok", "data":serialized_product.data}, status=status.HTTP_200_OK)
    
    

