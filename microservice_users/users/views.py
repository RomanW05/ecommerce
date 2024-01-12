from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializer import ResisterSerializer

# Create your views here.


class RegisterUser(generics.GenericAPIView):
    register_serializer = ResisterSerializer
    permission_class = (permissions.AllowAny,)