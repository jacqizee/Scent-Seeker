from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

Users = get_user_model()

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        pass
    
class LoginView(APIView):
    def get(self, request):
        pass