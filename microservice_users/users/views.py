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


class RegisterUser(generics.GenericAPIView):
    register_serializer = ResisterSerializer
    permission_class = (permissions.AllowAny,)

    def post(self, request):
        print(request.data)
        serializer = ResisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_registration_email(request.data['email'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginUser(generics.GenericAPIView):
    login_serializer = LoginSerializer
    permission_class = (permissions.AllowAny,)

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            email = request.data.get('email')
            user = User.objects.filter(email=email)
            if user is None:
                return Response({"message":'User not found'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message":'User found'}, status=status.HTTP_200_OK)
        else:
            return Response({"message":'Credentials not valid'}, status=status.HTTP_400_BAD_REQUEST)
