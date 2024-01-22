from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
from django.core.cache import cache
from rest_framework_simplejwt.tokens import UntypedToken
import logging
from django.conf import settings

logger = logging.getLogger('main')


def send_registration_email(user_email):
    send_mail(
        "Welcome",
        "Welcome to our ecommerce",
        "from@example.com",
        [user_email],
        fail_silently=False,
    )


class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.date_joined = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


def cache_blacklisted_token(token):
    try:
        untyped_token = UntypedToken(token)
        jti = untyped_token['jti']
        cache.set(jti, 'blacklisted', timeout=settings.EXPIRE_TIME_REFRESH_IN_SECS)
        logger.debug(f'Blacklisted token cached: {e}')
    except Exception as e:
        logger.debug(f'Error in caching token: {e}')

def is_token_blacklisted(token):
    try:
        untyped_token = UntypedToken(token)
        jti = untyped_token['jti']
        if cache.get(jti) == 'blacklisted':
            return True
        else:
            return False
    except Exception as e:
        logger.info(f"Error checking token: {e}")
        return True