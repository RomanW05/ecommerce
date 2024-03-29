import logging
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


from .authentication import JWTAuthentication
from .forms import PasswordResetForm
from .handlers import send_registration_email, cache_blacklisted_token, is_token_blacklisted, send_custom_email
from .serializer import (LoginSerializer, ResisterSerializer, ForgotPasswordSerializer)


User = get_user_model()
logger = logging.getLogger('main')


class RegisterUser(generics.GenericAPIView):
    serializer_class = ResisterSerializer
    permission_class = (permissions.AllowAny,)
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({"message": f"User already created {e}"}, status=status.HTTP_400_BAD_REQUEST)
            send_registration_email(serializer.validated_data['email'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_class = (permissions.AllowAny,)
    authentication_classes = []

    def post(self, request):
        logger.info(f'User ')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get('password')

            user = User.objects.filter(email=email).first()
            logger.info(type(user))
            if user is None:
                username = email.split('@')[0]
                user = User.objects.filter(username=username).first()
                if user is None:
                    return Response({"message":'User not found'}, status=status.HTTP_400_BAD_REQUEST)
            if not user.check_password(password):
                return Response({"message":'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
            logger.info(user.pk)
            jwt_token = JWTAuthentication.create_refresh_jwt(user)
            
            logger.info(f'User logged in: {user.email}')
            return Response({"data":jwt_token}, status=status.HTTP_200_OK)


class TestToken(generics.GenericAPIView):

    def post(self, request):
        logger.debug(request.data)
        refresh = request.data.get('refresh')
        if is_token_blacklisted(refresh):
            return Response({"message":"Session expired"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message":"Token accepted"}, status=status.HTTP_200_OK)


class LogoutUser(generics.GenericAPIView):

    def post(self, request):
        refresh = request.data.get('refresh')
        if refresh is None:
            return Response({"message":'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            cache_blacklisted_token(refresh)
            return Response({"message":"User logged out"}, status=status.HTTP_200_OK)
        except TokenError as e:
            logger.debug(e)
            return Response({"message":f'Invalid refresh token or already invalid'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.debug(e)
            return Response({"message":'Invalid method'}, status=status.HTTP_400_BAD_REQUEST)


class AlwaysOK(generics.GenericAPIView):
    authentication_classes = []
    def get(self, request):
        return Response({"message": "ok"}, status=status.HTTP_200_OK)


class ForgotPassword(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            
            if user is None:
                return Response({"message": "User not found"}, status=status.HTTP_400_NOT_FOUND)
            reset_token = JWTAuthentication.create_password_reset_jwt(user)
            send_custom_email(user, 'forgotten_password', reset_token=reset_token)

            return Response({"message": "Reset password sent to email"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Not valid"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(generics.GenericAPIView):
    
    def post(self, request):
        form = PasswordResetForm(request.data)
        if form.is_valid():
            user_id = request.user.get('user_id') if hasattr(request, 'user') and request.user else None
            if user_id is None:
                return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=user_id)
            if user is None:
                return Response({"message":"No user found"}, status=status.HTTP_400_BAD_REQUEST)

            jwt_token = request.META.get('HTTP_AUTHORIZATION')
            if not JWTAuthentication.is_token_valid(jwt_token.split()[1]):
                return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
            
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            return Response({"message": 'Passwords changed'}, status=status.HTTP_202_ACCEPTED)
        else:
            logger.debug(form.errors)
            return Response({"message": 'Invalid password fields'}, status=status.HTTP_400_BAD_REQUEST)
