from django.db import models
from django.contrib.auth.models import User
from subscriptions.models import SubscriptionType
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    subscription_type = models.ForeignKey(SubscriptionType,on_delete=models.CASCADE,related_name='videos')
    view_count = models.IntegerField()

class Comment(models.Model):
    content = models.textField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='ratings')
    created_at = models.DateTimeField(auto_now_add=True)

