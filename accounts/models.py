from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_staff = False

class AdminUser(AbstractUser):
    is_staff = True
    is_superuser = True