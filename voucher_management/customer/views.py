from django.shortcuts import render
from rest_framework import viewsets
from customer.models import Wallet
from rest_framework.decorators import action
from rest_framework.response import Response
from customer.serializers.redeem_voucher import RedeemVoucherSerializer
from customer.serializers.buy_voucher import BuyVoucherSerializer
from rest_framework.permissions import IsAuthenticated


class WalletViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def list_vouchers(self, request):
        wallets = (
            Wallet.objects.filter(customer=request.user).select_related("voucher").all()
        )

        results = [
            {
                "voucher_id": i.voucher.id,
                "voucher_name": i.voucher.name,
                "balance": i.balance,
            }
            for i in wallets
        ]

        return Response(data=results, status=200)

    @action(detail=False, methods=["post"])
    def redeem_vouchers(self, request):
        serializer = RedeemVoucherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        voucher = serializer.validated_data["voucher"]
        amount = serializer.validated_data["amount"]

        user = self.request.user
        wallet = Wallet.objects.filter(voucher=voucher, customer=user).first()

        if wallet is None or wallet.balance == 0:
            return Response(
                data={"message": "You don't have this kind of voucher."}, status=400
            )

        if wallet.balance < amount:
            wallet.balance = 0
            wallet.save()
            return Response(data={"message": "The voucher was fully used."}, status=200)
        wallet.balance -= amount
        wallet.save()
        return Response(
            data={
                "message": f"You have used voucher successfully. The balance is {wallet.balance}"
            },
            status=200,
        )

    @action(detail=False, methods=["post"])
    def buy_voucher(self, request):
        user = self.request.user
        serializer = BuyVoucherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        voucher = serializer.validated_data["voucher"]

        exist_wallet = Wallet.objects.filter(customer=user, voucher=voucher).first()
        if exist_wallet is not None:
            exist_wallet.balance += voucher.get_amount
            exist_wallet.save()
            return Response(
                data={
                    "balance": exist_wallet.balance,
                    "voucher_name": voucher.name,
                },
                status=200,
            )
        else:
            Wallet.objects.create(
                customer=user,
                voucher=voucher,
                balance=voucher.get_amount,
            )
            return Response(
                data={
                    "balance": voucher.get_amount,
                    "voucher_name": voucher.name,
                },
                status=200,
            )
