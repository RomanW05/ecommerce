from os import name
from .models import Categories, Products, ProductImages, Sizes, Colors, Discounts, ImageFormat, Images
from django.conf import settings


def populate_item():
    # category = Categories.objects.create(name='Men pants')
    category = Categories.objects.filter(name='Men pants').first()
    # color = Colors.objects.create(name='Blue', hexadecimal='0000ff')
    color = Colors.objects.filter(name='Blue').first()
    # size = Sizes.objects.create(size='M')
    size = Sizes.objects.filter(size='M').first()
    # image_format = ImageFormat.objects.create(name='Mobile')
    image_format = ImageFormat.objects.filter(name='Mobile')
    # image = Images.objects.create(path=f'{settings.STATIC_URL}/images/sustainable-apparel-coalition.jpeg', format_id=image_format)
    # image = Images.objects.filter(format_id=image_format).first()
    product = Products.objects.create(category=category, color=color, description='mock description', name='Men jeans pants', size=size, sku='1234567890123')
    # ProductImages.objects.create(image=image.pk, product=product.pk)