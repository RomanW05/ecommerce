from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Categories(models.Model):
    name = models.CharField(_('Name'), max_length=60, unique=True)


class Colors(models.Model):
    name = models.CharField(_('Name'), max_length=60, unique=True)
    hexadecimal = models.CharField(_('Hexadecimal'), max_length=60, unique=True)


class Sizes(models.Model):
    size = models.CharField(_('Size'), max_length=60, unique=True)


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category_id')
    color = models.ForeignKey(Colors, on_delete=models.RESTRICT, max_length=60)
    description = models.CharField(_('Description'), max_length=60)
    name = models.CharField(_('Name'), max_length=60)
    size = models.ForeignKey(Sizes, on_delete=models.RESTRICT, max_length=60)
    sku = models.CharField(('SKU'), max_length=60, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Discounts(models.Model):
    percentage = models.CharField(_('Percentage'), max_length=60)
    name = models.CharField(_('Name'), max_length=60, unique=True)
    duration = models.CharField(_('Duration'), max_length=60)


class ImageFormat(models.Model):
    name = models.CharField(_('Image format'), max_length=60, unique=True)


class Images(models.Model):
    format_id = models.ForeignKey(ImageFormat, on_delete=models.RESTRICT, related_name='image_format_id')
    path = models.CharField(_('Image path'), max_length=60, unique=True)


class ProductImages(models.Model):
    image = models.ForeignKey(Images, on_delete=models.RESTRICT, related_name='image_id')
    product = models.ForeignKey(Products, on_delete=models.RESTRICT, related_name='product_id')
    