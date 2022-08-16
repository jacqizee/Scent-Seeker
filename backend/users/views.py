from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
from django.conf import settings
import jwt
from datetime import datetime, timedelta

User = get_user_model()

# Create your views here.

# Endpoint - /register/
# Methods: POST
class RegisterView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        
        try:
            user.is_valid(raise_exception=True)
            user.save()
            return Response({'message': 'Registration Successful'}, status.HTTP_201_CREATED)
        except ValidationError:
            return Response(user.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response(e.args[0], status.HTTP_422_UNPROCESSABLE_ENTITY)
            
# Endpoint - /login/
# Methods: POST
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials.'})
        
        if not User.check_password(user_to_login, password):
            raise PermissionDenied({'message': 'Invalid credentials.'})

        token = jwt.encode({
            'sub': user_to_login.id,
            'exp': datetime.now() + timedelta(weeks = 1)
        }, settings.SECRET_KEY, 'HS256')

        return Response(
            {'message': 'Login successful', 'token': token},
            status.HTTP_202_ACCEPTED)