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


class Country(models.Model):
    name = models.CharField('Country', max_length=60, unique=True)
    
    def __str__(self):
        return self.name


class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='province_id')
    name = models.CharField('Province name', max_length=60)

    def __str__(self):
        return self.name


class ZipCode(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='zip_code_id')
    zipcode = models.CharField('Zip code', max_length=20, unique=True)
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_id')
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    street_block_number = models.CharField('Street block', max_length=60)
    street_floor_number = models.CharField('Street floor', max_length=60)
    street_house_number = models.CharField('Street house number', max_length=60)
    street_name = models.CharField('Street name', max_length=60)
 
    



