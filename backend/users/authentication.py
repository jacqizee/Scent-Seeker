from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

User = get_user_model()

class JWTAuthentication(BasicAuthentication):
    # overwrite basicauthentication's authenticate method for custom auth
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        if not auth_header.startswith('Bearer '):
            raise PermissionDenied('Token invalid.')

        token = auth_header.replace('Bearer ', '')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ['HS256'])
            user = User.objects.get(pk=payload['sub'])
        except jwt.InvalidTokenError:
            raise PermissionDenied('Token invalid')
        except User.DoesNotExist:
            raise PermissionDenied('Token for invalid user.')

        return (user, token)