from rest_framework import status
from django.shortcuts import get_object_or_404
from subscriptions.models import SubscriptionType
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serlializers import CreatePaymentSerilizer
from .models import PaymentHistory

# Create your views here.

class PaymentRequestAPI(APIView):
    def post(self,request):
        data = request.data

        serilized = CreatePaymentSerilizer(data=data)

        if not serilized.is_valid():
            return Response(serilized.errors,status=status.HTTP_400_BAD_REQUEST)

        id = serilized.validated_data.get('subscription_type_id')

        subscription_type = get_object_or_404(SubscriptionType,pk=id)

        payment = PaymentHistory.objects.create(
            user=request.user,
            subscription_type=subscription_type,
            amount=subscription_type.price,
            status='PENDING',
        )

        


