from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Products

import logging

logger = logging.getLogger('main')

# Create your views here.

class ProductInfo(generics.GenericAPIView):
    permission_class = (permissions.AllowAny,)
    authentication_classes = []
    def get(self, request):
        product_id = request.GET.get("product_id")
        logger.info(product_id)
        product_info = Products.objects.filter(id=product_id)
        if product_info is None:
            return Response({'message': "Product not found"}, status=status.HTTP_400_NOT_FOUND)
        return Response({'message': "ok", "data":product_info}, status=status.HTTP_200_OK)
    


