from rest_framework import generics, status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from rest_framework_simplejwt.tokens import BlacklistMixin

from confluent_kafka import Producer
from django.http import HttpResponseRedirect
from django.shortcuts import render
import json
import pickle

from .authentication import HasRestrictedScope, HasFullScope, IsWhitelisted
from .functions import create_request_meta_json_object, kafka_send_message
from .serializer import RequestSerializer, RegisterSerializer, RestrictedAccessSerializer, OTPSerializer, DeleteUserSerializer

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


kafka_producer = Producer({'bootstrap.servers': 'kafka1:19091'})


class Home(APIView):
    serializer_class = RequestSerializer
    topic = 'analytics'

    def get(self, request, topic):
        request_dictionary = create_request_meta_json_object(request.META)
        # serializer = self.serializer_class(data=request_dictionary)
        # if not serializer.is_valid():
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        
        print(type(request.headers), 'request.headers', request.headers)
        data = {"request_headers": request.headers, "request_body":request_dictionary}
        kafka_send_message(kafka_producer, topic, json.dumps(data))
        return Response(status=status.HTTP_200_OK)


class Index(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    

# class Register(generics.ListCreateAPIView):
#     serializer_class = RegisterSerializer

#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(status=status.HTTP_409_CONFLICT)
#         return Response(status=status.HTTP_201_CREATED)
    
#     def get(self, request):
#         return Response(status=status.HTTP_200_OK)


# class Login(generics.ListCreateAPIView):
#     serializer_class = RestrictedAccessSerializer
#     template_login = "login.html"
#     template_validate = "validate.html"

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.main(attrs={
#             'username': request.data['username'],
#             'password': request.data['password']
#             })

#         return Response(data, status=status.HTTP_202_ACCEPTED)

#     def get(self, request):
#         return Response(status=status.HTTP_200_OK)


# class verifyOTP(APIView):
#     serializer_class = OTPSerializer
#     authentication_classes = [JWTTokenUserAuthentication]
#     permission_classes = [IsAuthenticated, HasRestrictedScope, IsWhitelisted]

#     def post(self, request):
#         JWT_authenticator = JWTAuthentication()
#         response = JWT_authenticator.authenticate(request)
#         if response is None:
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
#         if not request.data["otp"]:
#             return Response({'Error':'OTP missing'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = self.serializer_class(data={'otp':request.data["otp"], 'auth':request.headers['Authorization']})
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#     def get(self, request):
#         return Response(status=status.HTTP_200_OK)


# class Logout(generics.GenericAPIView):
#     authentication_classes = [JWTTokenUserAuthentication]
#     permission_classes = [IsAuthenticated, HasFullScope, IsWhitelisted]

#     def post(self, request):
#         JWT_authenticator = JWTAuthentication()
#         response = JWT_authenticator.authenticate(request)
#         if response is None:
#             raise BaseException
#         else:
#             user, token = response

#         response = BlacklistMixin.blacklist(token)
#         if response[1] == True:  # Token added to blacklist
#             print('token blacklisted')
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             print('token not blacklisted')
#             return Response(status=status.HTTP_304_NOT_MODIFIED)
    

# class DeleteAccount(generics.ListCreateAPIView):
#     serializer_class = DeleteUserSerializer
#     authentication_classes = [JWTTokenUserAuthentication]
#     permission_classes = [IsAuthenticated, HasFullScope, IsWhitelisted]

#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(status=status.HTTP_205_RESET_CONTENT)
    
#     def get(self, request):
#         return Response(status=status.HTTP_200_OK)