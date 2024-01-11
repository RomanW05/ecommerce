from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, editable=False)
    username = models.CharField('Username', unique=True)
    email = models.EmailField('Email address', unique=True)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)
    blocked_status = models.BooleanField('Blocked status', default=False)
    name = models.CharField('Name', max_length=60, null=True)
    surname = models.CharField('Surname', max_length=60, null=True)
    phone_number = models.CharField('Phone number', max_length=20, unique=True, null=True)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_id')
    country_id =  models.ForeignKey
    province_id =  models.ForeignKey
    street_block_number = models.CharField('Surname', max_length=60)
    street_floor_number = models.CharField('Surname', max_length=60)
    street_house_number = models.CharField('Surname', max_length=60)
    street_name = models.CharField('Surname', max_length=60)
    zip_code_id =  models.ForeignKey

class Country(models.Model):
    id = models.CharField(primary_key=True, editable=False)
    country = models.CharField('Country', max_length=60, unique=True)

class ZipCode(models.Model):
    id = models.CharField(primary_key=True, editable=False)
    zipcode = models.CharField('Zip code', max_length=20, unique=True)
    country = models.ForeignKey(Country, related_name='zip_code_id')

class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='province_id')
    name = models.CharField('Province name', max_length=60)
    












    
    