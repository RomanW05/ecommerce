from rest_framework import generics, status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from rest_framework_simplejwt.tokens import BlacklistMixin

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .authentication import HasRestrictedScope, HasFullScope, IsWhitelisted
from .serializer import RegisterSerializer, RestrictedAccessSerializer, OTPSerializer, DeleteUserSerializer
"""
path('home/', views.Home.as_view(), name="home"),
path('login/', views.Login.as_view(), name="login"),
path('logout/', views.Logout.as_view(), name="logout"),
path('register/', views.Register.as_view(), name="register"),
path('verify_otp/', views.verifyOTP.as_view(), name='verify otp'),

path('profile/', views.Profile.as_view(), name="profile"),
path('delete_account/', views.DeleteAccount.as_view(), name="delete user"),

path('explore/', views.Explore.as_view(), name="explore"),
path('product/<pk:id>', views.Product.as_view(), name="product"),
path('product_image/<pk:id>', views.ProductImage.as_view(), name="product image"),

path('cart/', views.Product.as_view(), name="cart"),
path('checkout/', views.Checkout.as_view(), name="checkout"),
path('verify_checkout/', views.Product.as_view(), name="verify checkout"),
"""