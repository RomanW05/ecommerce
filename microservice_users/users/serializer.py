import logging
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers


User = get_user_model()
logger = logging.getLogger('main')


class ResisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    def validate(self, data):
        user_email = User.objects.filter(email=data.get('email'))
        if user_email.exists():
            raise ValidationError("Email already registered")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        logger.info(f'Created new user {user.email}')
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

