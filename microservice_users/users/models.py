from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .manager import MyUserManager
# Create your models here.


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, unique=True, blank=True, null=True)
    is_blocked = models.BooleanField('Blocked status', default=False)

    objects = MyUserManager()



