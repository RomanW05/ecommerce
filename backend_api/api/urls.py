'''
ROUTES:
home
login
logout
register
explore
checkout
product
profile
api for explore
api for product images
'''
from . import views
from django.urls import path


app_name = 'api'

urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('verify_otp/', views.verifyOTP.as_view(), name='verify otp'),

    path('profile/', views.Profile.as_view(), name="profile"),
    path('delete_account/', views.DeleteAccount.as_view(), name="delete user"),

    path('explore/', views.Explore.as_view(), name="explore"),
    path('product/<pk:id>', views.Product.as_view(), name="product"),

    path('cart/', views.Product.as_view(), name="cart"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('verify_checkout/', views.Product.as_view(), name="verify checkout"),
    
    
    
]