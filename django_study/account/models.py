from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
# Create your models here.