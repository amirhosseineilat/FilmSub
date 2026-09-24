from rest_framework import serializers
from subscriptions.models import SubscriptionType

class CreatePaymentSerilizer(serializers.Serializer):
    subscription_type_id = serializers.IntegerField()

    def validate_subscription_type_id(self,value):
        if not SubscriptionType.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                'subscription does not exist'
            )

        return value
