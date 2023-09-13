from rest_framework import generics, status
from rest_framework.response import Response

from easy_trade.stock.models import Stock
from easy_trade.stock.serializers import StockSerializer


class StockView(generics.ListAPIView):
    def list(self, *args, **kwargs):
        queryset = Stock.objects.filter()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
