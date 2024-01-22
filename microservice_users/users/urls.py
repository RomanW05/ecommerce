from django.urls import path

from .views import (RegisterUser, LoginUser, TestToken, BlacklistRefreshView)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='Register new user'),
    path('login/', LoginUser.as_view(), name='Login'),
    path('test_token/', TestToken.as_view(), name='Test token'),
    path('logout/', BlacklistRefreshView.as_view(), name="logout"),
]