from rest_framework import serializers

class CreatePaymentSerilizer(serializers.Serializer):
    subscription_type_id = serializers.IntegerField()


