from rest_framework import serializers

from voucher.models.voucher import Voucher


class BuyVoucherSerializer(serializers.Serializer):
    voucher = serializers.PrimaryKeyRelatedField(queryset=Voucher.objects.all())
