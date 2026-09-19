from django.shortcuts import render
from rest_framework.generics import CreateAPIView 
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.

User = get_user_model()

class Register(CreateAPIView):
    model = User
    serializer_class = RegisterSerializer

class UserActive(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        data = {
            "username":request.user.username,
            "is_authenticated":request.user.is_authenticated
        }
        return Response(data,status=status.HTTP_200_OK)

