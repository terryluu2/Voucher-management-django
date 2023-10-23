from django.db import models
from store.models.store import Store


class Voucher(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    numbers = models.IntegerField(default=0)
    buy_amount = models.IntegerField(default=10)
    get_amount = models.IntegerField(default=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
