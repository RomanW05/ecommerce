from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, editable=False)
    username = models.CharField('Username', unique=True)
    email = models.EmailField('Email address', unique=True)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)
    blocked_status = models.BooleanField('Blocked status', default=False)
    name = models.CharField('Name', max_length=60)
    surname = models.CharField('Surname', max_length=60)
    phone_number = models.CharField('Phone number', max_length=20, unique=True)




    
    