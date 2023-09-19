from rest_framework import serializers

from easy_trade.stock.models import HistoricalStock, Stock, Transaction, Wallet


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class StockWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["name", "code", "current_price"]


class WalletSerializer(serializers.ModelSerializer):
    stock = StockWalletSerializer()

    class Meta:
        model = Wallet
        exclude = ["user"]


class HistoricalStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalStock
        exclude = ["stock"]


class TransactionSerializer(serializers.ModelSerializer):
    stock = StockWalletSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"


class CreateTransactionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=["buy", "sale"])

    class Meta:
        model = Transaction
        fields = ["stock", "quantity", "type"]
