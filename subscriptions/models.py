from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SubscriptionType(models.Model):
    SUB_TYPE = [
        ('FREE','Free'),
        ('BRONZE','Bronze'),
        ('SILVER','Silver'),
        ('GOLD','Gold'),
    ]
    type = models.CharField(max_length=20,choices=SUB_TYPE)
    price = models.FloatField()
    level = models.IntegerField()
    duration = models.DurationField()

class Subscription(models.Model):
    SUB_STATUS = [
        ('EXPIRED','Expired'),
        ('CANCELLED','Cancelled'),
        ('ACTIVE','Active'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='subscriptions')
    subscription_type = models.ForeignKey(SubscriptionType,on_delete=models.CASCADE,related_name='subscriptions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30,choices=SUB_STATUS)