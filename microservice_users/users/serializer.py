import logging
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import User
# from django.contrib.auth.models import User


User = get_user_model()
logger = logging.getLogger('main')

class ResisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email',)
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    def validate_email(self, data):
        logger.debug(f'Validating {data}')
        user_email = User.objects.filter(email=data)
        if user_email.exists():
            raise ValidationError("Email already registered")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], date_joined=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        logger.info(f'Created new user {validated_data}')
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')