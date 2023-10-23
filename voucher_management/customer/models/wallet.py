from django.db import models
from customer.models.customer import Customer


class Wallet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    voucher = models.ForeignKey(
        "voucher.Voucher", on_delete=models.SET_NULL, null=True, blank=True
    )
    balance = models.IntegerField()
