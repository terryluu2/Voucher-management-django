from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    balance = models.IntegerField(null=True, blank=True, default=0)
