from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='wallet')
    balance = models.IntegerField()