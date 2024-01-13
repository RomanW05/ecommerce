from django.urls import path

from .views import (RegisterUser, LoginUser)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='Register new user'),
    path('login/', LoginUser.as_view(), name='Login'),
]