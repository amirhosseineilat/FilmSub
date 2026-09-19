from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

# Create your views here.

User = get_user_model()

class Register(CreateAPIView):
    model = User
    serializer_class = RegisterSerializer