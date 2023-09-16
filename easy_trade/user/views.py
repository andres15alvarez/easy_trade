from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from easy_trade.account.models import Account
from easy_trade.user.serializers import UserSerializer


class UserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Account.objects.create(user=user, balance=0)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
