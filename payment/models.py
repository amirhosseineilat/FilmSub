from django.db import models
from subscriptions.models import Subscription
from django.contrib.auth import get_user_model

User = get_user_model()

class Wallet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='wallet')
    balance = models.IntegerField()

class PaymentHistory(models.Model):
    PAYMENT_STATUS = [
        ('SUCCESS','Success'),
        ('FAILED','Failed'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='payment_history')
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE,related_name='payment_history')
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='payment_history')
    amount = models.IntegerField()
    status = models.CharField(max_length=30,choices=PAYMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)    