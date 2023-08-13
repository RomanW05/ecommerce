from rest_framework import generics, status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from rest_framework_simplejwt.tokens import BlacklistMixin

from django.http import HttpResponseRedirect
from django.shortcuts import render
import json
from kafka import KafkaConsumer, KafkaProducer
import pickle


from .authentication import HasRestrictedScope, HasFullScope, IsWhitelisted
from .serializer import RegisterSerializer, RestrictedAccessSerializer, OTPSerializer, DeleteUserSerializer
"""
path('home/', views.Home.as_view(), name="home"),

path('profile/', views.Profile.as_view(), name="profile"),

path('explore/', views.Explore.as_view(), name="explore"),
path('product/<pk:id>', views.Product.as_view(), name="product"),
path('product_image/<pk:id>', views.ProductImage.as_view(), name="product image"),

path('cart/', views.Product.as_view(), name="cart"),
path('checkout/', views.Checkout.as_view(), name="checkout"),
path('verify_checkout/', views.Product.as_view(), name="verify checkout"),
"""
from confluent_kafka import Producer
import socket



# producer.produce(topic, key="key", value="value")
def kafka_produce(request, topic):
    # conf = {'bootstrap.servers': "host1:9092,host2:9092",
    #     'client.id': socket.gethostname()}
    # producer = Producer(conf)
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    message = request
    serialized_data = pickle.dumps(message, pickle.HIGHEST_PROTOCOL)
    producer.send(topic, serialized_data)
    return status.HTTP_202_ACCEPTED


class Home(generics.ListCreateAPIView):
    def get(self, request):
        topic = 'analytics'
        kafka_produce(request, topic)
        return Response(status=status.HTTP_200_OK)



class Register(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_201_CREATED)
    
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class Login(generics.ListCreateAPIView):
    serializer_class = RestrictedAccessSerializer
    template_login = "login.html"
    template_validate = "validate.html"

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.main(attrs={
            'username': request.data['username'],
            'password': request.data['password']
            })

        return Response(data, status=status.HTTP_202_ACCEPTED)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class verifyOTP(APIView):
    serializer_class = OTPSerializer
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated, HasRestrictedScope, IsWhitelisted]

    def post(self, request):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if response is None:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        if not request.data["otp"]:
            return Response({'Error':'OTP missing'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data={'otp':request.data["otp"], 'auth':request.headers['Authorization']})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class Logout(generics.GenericAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated, HasFullScope, IsWhitelisted]

    def post(self, request):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if response is None:
            raise BaseException
        else:
            user, token = response

        response = BlacklistMixin.blacklist(token)
        if response[1] == True:  # Token added to blacklist
            print('token blacklisted')
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            print('token not blacklisted')
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    

class DeleteAccount(generics.ListCreateAPIView):
    serializer_class = DeleteUserSerializer
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated, HasFullScope, IsWhitelisted]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_205_RESET_CONTENT)
    
    def get(self, request):
        return Response(status=status.HTTP_200_OK)