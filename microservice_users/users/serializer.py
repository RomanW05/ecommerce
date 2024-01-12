from django.contrib.auth import get_user_model
from rest_framework import  serializers

from .models import User

User = get_user_model()

class ResisterSerializer:
    class meta:
        model = User
        fields = ('id','email', 'password',)
        extra_kwargs = {
            'password':{'write_only': True},
        }