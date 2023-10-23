from rest_framework import serializers


class CustomSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    balance = serializers.IntegerField(required=True)
    is_staff = serializers.BooleanField(required=True)
