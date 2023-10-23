from rest_framework import serializers
from voucher.models import Voucher


class RedeemVoucherSerializer(serializers.Serializer):
    voucher = serializers.PrimaryKeyRelatedField(queryset=Voucher.objects.all())
    amount = serializers.IntegerField(required=True)
