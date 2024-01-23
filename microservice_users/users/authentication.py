from datetime import datetime, timedelta
import jwt
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, ParseError

from .handlers import is_token_blacklisted
import logging


logger = logging.getLogger('main')
User = get_user_model()


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            raise AuthenticationFailed('No token provided')

        jwt_token = self.get_the_token_from_header(jwt_token)  # clean the token

        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()

        # Get the user from the database
        user_id = payload.get('user_id')
        if user_id is None:
            raise AuthenticationFailed('User identifier not found in JWT')
        
        if is_token_blacklisted(jwt_token):
            raise AuthenticationFailed('Token expired')
        
        return payload, None

 
    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_refresh_jwt(cls, user):
        # Create the JWT payload
        payload = {
            'user_id': user.pk,
            'exp': datetime.utcnow() + timedelta(seconds=settings.REFRESH_TOKEN_LIFETIME),
            'iat': datetime.utcnow(),
            'jti': str(uuid.uuid4())
        }
        # Encode the JWT with your secret key
        refresh_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return refresh_token
    
    @classmethod
    def create_access_jwt(cls, user):
        # Create the JWT payload
        payload = {
            'user_id': user.pk,
            'exp': (datetime.utcnow() + timedelta(seconds=settings.REFRESH_TOKEN_LIFETIME)),
            'iat': datetime.utcnow(),
            'jti': str(uuid.uuid4())
        }
        # Encode the JWT with your secret key
        access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return access_token


    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token

