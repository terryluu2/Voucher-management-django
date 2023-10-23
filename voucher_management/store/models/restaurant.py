from django.contrib.auth.models import AbstractUser
from django.db import models
from customer.models.wallet import Wallet


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
