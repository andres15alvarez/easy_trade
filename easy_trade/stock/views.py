from rest_framework import generics, status
from rest_framework.response import Response

from easy_trade.stock.models import HistoricalStock, Stock, Wallet
from easy_trade.stock.serializers import (
    HistoricalStockSerializer,
    StockSerializer,
    WalletSerializer,
)


class WalletView(generics.RetrieveAPIView):
    def get(self, request) -> Response:
        queryset = Wallet.objects.filter(user=request.user)
        serializer = WalletSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StockView(generics.ListAPIView):
    def list(self, request):
        queryset = Stock.objects.filter()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StockHistoricalView(generics.ListAPIView):
    def get_queryset(self):
        code = self.request.query_params.get("code")
        date_from = self.request.query_params.get("from")
        date_to = self.request.query_params.get("to")
        return HistoricalStock.objects.filter(
            day__range=(date_from, date_to), stock__code=code
        ).select_related("stock")

    def list(self, request):
        queryset = self.get_queryset()
        serializer = HistoricalStockSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
