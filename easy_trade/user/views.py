from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from easy_trade.account.models import Account
from easy_trade.user.serializers import UserPasswordSerializer, UserSerializer


class UserView(APIView):
    @permission_classes([AllowAny])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Account.objects.create(user=user, balance=0)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer = UserPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not check_password(serializer.validated_data["old"], request.user.password):
            return Response(
                {"error": "Contraseña antigua incorrecta"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
        request.user.password = make_password(serializer.validated_data["new"])
        request.user.save()
        return Response(status=status.HTTP_200_OK)
