from rest_framework import serializers

from voucher.models.voucher import Voucher


class VoucherSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(required=True)
    # balance = serializers.IntegerField(required=True)
    # is_staff = serializers.BooleanField(required=True)
    class Meta:
        fields = "__all__"
        model = Voucher

    def validate(self, attrs):
        if attrs["get_amount"] > 2 * attrs["buy_amount"]:
            raise serializers.ValidationError(
                "The “get” cannot be greater than double the “buy” price"
            )
        return super().validate(attrs)

    def validate_buy_amount(self, buy_amount):
        if buy_amount < 10:
            raise serializers.ValidationError("buy_amount must larger than 10")
        return buy_amount

    def validate_get_amount(self, get_amount):
        if get_amount > 5000:
            raise serializers.ValidationError("get_amount can not exceed 5000")
        return get_amount
