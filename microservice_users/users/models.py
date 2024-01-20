from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .manager import MyUserManager
# Create your models here.
    

class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, editable=False, max_length=16)
    username = models.CharField(_('Username'), unique=True, max_length=24)
    email = models.EmailField(_('Email address'), unique=True, max_length=64)
    date_joined = models.DateTimeField()
    blocked_status = models.BooleanField('Blocked status', default=False)
    name = models.CharField(_('Name'), max_length=60, null=True)
    surname = models.CharField(_('Surname'), max_length=60, null=True)
    phone_number = models.CharField(_('Phone number'), max_length=20, unique=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # other required fields besides email, if any
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return False
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return False


class Country(models.Model):
    name = models.CharField(_('Country'), max_length=60, unique=True)
    
    def __str__(self):
        return self.name


class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='province_id')
    name = models.CharField(_('Province'), max_length=60)

    def __str__(self):
        return self.name


class ZipCode(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='zip_code_id')
    zipcode = models.CharField(_('Zip code'), max_length=20, unique=True)
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_id')
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    street_block_number = models.CharField(_('Street block'), max_length=60)
    street_floor_number = models.CharField(_('Street floor'), max_length=60)
    street_house_number = models.CharField(_('Street house number'), max_length=60)
    street_name = models.CharField(_('Street name'), max_length=60)
 
    



