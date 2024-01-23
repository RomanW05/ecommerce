from django.core.mail import send_mail
from datetime import datetime
from django.core.cache import cache
from rest_framework_simplejwt.tokens import UntypedToken, RefreshToken

import logging
from django.conf import settings
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken


logger = logging.getLogger('main')


def send_registration_email(user_email):
    send_mail(
        "Welcome",
        "Welcome to our ecommerce",
        "from@example.com",
        [user_email],
        fail_silently=False,
    )


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
            return BlacklistedToken.objects.filter(token__jti=jti).exists()
    except Exception as e:
        logger.info(f"Error checking token: {e}")
        return True

