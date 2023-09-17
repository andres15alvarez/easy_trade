from rest_framework import serializers

from easy_trade.account.models import Account, AccountTransaction, Card


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["balance"]


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ["user"]
        extra_kwargs = {"cvv": {"write_only": True}}


class AccountTransactionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=["deposit", "withdraw"])

    class Meta:
        model = AccountTransaction
        exclude = ["account"]
