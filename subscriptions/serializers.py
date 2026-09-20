from rest_framework import serializers
from .models import SubscriptionType,Subscription
from django.contrib.auth import get_user_model

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = [
            'type',
            'price',
            'level',
            'duration',
        ]

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            'subscriptionType',
        ]
     