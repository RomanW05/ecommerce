import logging
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Products

logger = logging.getLogger('main')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
    
