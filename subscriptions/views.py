from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from rest_framework import serializers, status
from .models import Subscription,SubscriptionType
from .serializers import SubscriptionSerializer,SubscriptionTypeSerializer
from rest_framework.views import APIView, Response 
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView

# Create your views here.

class SubscriptionTypeListCreateAPIView(ListCreateAPIView):

    serializer_class = SubscriptionTypeSerializer

    def get_queryset(self):
        return SubscriptionType.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method == 'POST':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class SubscriptionTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionTypeSerializer

    def get_queryset(self):
            return SubscriptionType.objects.all()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method in ['PATCH','PUT']:
            permission_classes = [IsAdminUser]

        elif self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        user = self.request.user
        subscription_type = serializer.validated_data['subscriptionType']
        wallet = user.wallet

        if wallet.balance < subscription_type.price:
            raise serializers.ValidationError("Insufficient balance in wallet.")

        with transaction.atomic():
            wallet.balance -= subscription_type.price
            wallet.save()

            Subscription.objects.create(user=user,
                subscriptionType=subscription_type,
                start_time=timezone.now(),
                end_time=timezone.now() + subscription_type.duration,
                status='ACTIVE')

            