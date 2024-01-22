import logging

from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError

from .authenticate import get_tokens_for_user
from .handlers import send_registration_email, cache_blacklisted_token, is_token_blacklisted
from .serializer import (
    LoginSerializer,
    ResisterSerializer, )

from .models import User
# Create your views here.

User = get_user_model()
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

# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.utils.decorators import method_decorator
class LoginUser(generics.GenericAPIView):
    login_serializer = LoginSerializer
    permission_class = (permissions.AllowAny,)

    # @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        logger.info(f'User logged in: {request.data}')
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({"message":'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(password):
            return Response({"message":'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)

        tokens = get_tokens_for_user(user)
        logger.info(f'User logged in: {user}')
        return Response({"data":tokens}, status=status.HTTP_200_OK)



class TestToken(generics.GenericAPIView):
    permission_class = (permissions.IsAuthenticated,)

    def post(self, request):
        access = request.headers['Authorization'].split(' ')[1]
        if is_token_blacklisted(access):
            return Response({"message":"Session expired"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message":"Token accepted"}, status=status.HTTP_200_OK)


class BlacklistRefreshView(generics.GenericAPIView):
    permission_class = (permissions.IsAuthenticated,)

    def post(self, request):
        refresh = request.data.get('refresh')
        access = request.headers['Authorization'].split(' ')[1]
        if refresh is None:
            return Response({"message":'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            cache_blacklisted_token(refresh)
            cache_blacklisted_token(access)
            return Response({"message":"token invalidated"}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({"message":f'Invalid refresh token or already invalid {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        