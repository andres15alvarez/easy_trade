from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from easy_trade.account.models import Account, AccountTransaction, Card
from easy_trade.account.serializers import (
    AccountSerializer,
    AccountTransactionSerializer,
    CardSerializer,
)


class AccountView(generics.RetrieveAPIView):
    def get(self, request):
        queryset = Account.objects.get(user=request.user)
        serializer = AccountSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardView(APIView):
    def post(self, request):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = Card.objects.filter(user=request.user, is_active=True)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountTransactionView(APIView):
    def get(self, request):
        queryset = AccountTransaction.objects.filter(account__user=request.user)
        serializer = AccountTransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = Account.objects.get(user=request.user)
        if serializer.validated_data["card"].user != request.user:
            return Response(
                {"error": "Tarjeta invalida"}, status=status.HTTP_406_NOT_ACCEPTABLE
            )
        if (
            serializer.validated_data["amount"] > account.balance
            and serializer.validated_data["type"] == "withdraw"
        ):
            return Response(
                {"error": "Saldo insuficiente"}, status=status.HTTP_406_NOT_ACCEPTABLE
            )
        transaction = serializer.save(account=account)
        if transaction.type == "deposit":
            account.balance += transaction.amount
        else:
            account.balance -= transaction.amount
        account.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
