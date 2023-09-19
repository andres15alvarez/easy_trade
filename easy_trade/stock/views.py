from django.conf import settings
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from easy_trade.account.models import Account
from easy_trade.stock.models import HistoricalStock, Stock, Transaction, Wallet
from easy_trade.stock.serializers import (
    CreateTransactionSerializer,
    HistoricalStockSerializer,
    StockSerializer,
    TransactionSerializer,
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


class StockTransactionView(APIView):
    def get(self, request):
        queryset = Transaction.objects.filter(
            Q(seller=request.user) | Q(buyer=request.user)
        )
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        stock = serializer.validated_data["stock"]
        account = Account.objects.get(user=request.user)
        wallet, _ = Wallet.objects.get_or_create(
            user=request.user, stock=stock, defaults={"quantity": 0}
        )
        if serializer.validated_data["type"] == "buy":
            amount = stock.current_price * serializer.validated_data["quantity"]
            if account.balance < amount:
                return Response(
                    {"error": "Saldo insuficiente"},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            account.balance -= amount
            account.save()
            wallet.quantity += serializer.validated_data["quantity"]
            wallet.save()
            Transaction.objects.create(
                seller_id=settings.BROKER_ID,
                price=stock.current_price,
                buyer=request.user,
                stock=serializer.validated_data["stock"],
                quantity=serializer.validated_data["quantity"],
            )
        if serializer.validated_data["type"] == "sale":
            amount = stock.current_price * serializer.validated_data["quantity"]
            if wallet.quantity < serializer.validated_data["quantity"]:
                return Response(
                    {"error": "Acciones insuficientes"},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            account.balance += amount
            account.save()
            wallet.quantity -= serializer.validated_data["quantity"]
            wallet.save()
            Transaction.objects.create(
                seller=request.user,
                price=stock.current_price,
                buyer_id=settings.BROKER_ID,
                stock=serializer.validated_data["stock"],
                quantity=serializer.validated_data["quantity"],
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
