from rest_framework import generics, status
from rest_framework.response import Response

from easy_trade.stock.models import HistoricalStock, Stock
from easy_trade.stock.serializers import HistoricalStockSerializer, StockSerializer


class StockView(generics.ListAPIView):
    def list(self, *args, **kwargs):
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

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HistoricalStockSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
