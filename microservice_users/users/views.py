import logging

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .handlers import send_registration_email
from .serializer import (
    LoginSerializer,
    ResisterSerializer, )

from .models import User
# Create your views here.

# User = get_user_model()
logger = logging.getLogger('main')

class RegisterUser(generics.GenericAPIView):
    serializer_class = ResisterSerializer
    permission_class = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                logger.info(f'Error while saving validator: {e}')
                return Response({"message": "User already created"}, status=status.HTTP_400_BAD_REQUEST)
            send_registration_email(request.data['email'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            logger.info(f'Serializer not valid: {serializer.errors}')
            return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(generics.GenericAPIView):
    login_serializer = LoginSerializer
    permission_class = (permissions.AllowAny,)

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            email = request.data.get('email')
            user = User.objects.filter(email=email).first()
            if user is None:
                return Response({"message":'User not found'}, status=status.HTTP_400_BAD_REQUEST)
            password = request.data.get('password')

            if not user.check_password(password):
                return Response({"message":'Wrong password', "error": login_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message":'Match'}, status=status.HTTP_200_OK)

        else:
            return Response({"message":'Credentials not valid'}, status=status.HTTP_400_BAD_REQUEST)
