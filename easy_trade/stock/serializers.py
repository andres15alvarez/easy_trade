from rest_framework.serializers import ModelSerializer

from easy_trade.stock.models import HistoricalStock, Stock


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class HistoricalStockSerializer(ModelSerializer):
    class Meta:
        model = HistoricalStock
        exclude = ["stock"]
