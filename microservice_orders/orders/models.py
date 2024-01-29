from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Orders(models.Model):
    date = models.DateTimeField(_('Date'), auto_now_add=True)
    order_id = models.CharField(_('Order id'), max_length=60, unique=True)
    payment_method_id = models.CharField(_('Payment Method id'), max_length=60, unique=True)
    status = models.CharField(_('Country'), max_length=60, unique=True)
    total = models.CharField(_('Country'), max_length=60, unique=True)
    tracking_number = models.CharField(_('Country'), max_length=60, unique=True)
    user_id = models.CharField(_('Country'), max_length=60, unique=True)























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
    id = models.CharField(primary_key=True, editable=False, max_length=10)
    phone_number = models.CharField(_('Phone number'), max_length=20, unique=True, null=True)
    user = models.IntegerField(_('User'))
    zipcode = models.CharField(_('Zip code'), max_length=60)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    street_block_number = models.CharField(_('Street block'), max_length=60)
    street_floor_number = models.CharField(_('Street floor'), max_length=60)
    street_house_number = models.CharField(_('Street house number'), max_length=60)
    street_name = models.CharField(_('Street name'), max_length=60)
 
    



