from rest_framework.serializers import ModelSerializer

from easy_trade.stock.models import HistoricalStock, Stock, Wallet


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class StockWalletSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = ["name", "code", "current_price"]


class WalletSerializer(ModelSerializer):
    stock = StockWalletSerializer()

    class Meta:
        model = Wallet
        exclude = ["user"]


class HistoricalStockSerializer(ModelSerializer):
    class Meta:
        model = HistoricalStock
        exclude = ["stock"]
