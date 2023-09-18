from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from easy_trade.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)


class UserPasswordSerializer(serializers.Serializer):
    old = serializers.CharField(max_length=128)
    new = serializers.CharField(max_length=128)

    def validate(self, attrs):
        if attrs["old"] == attrs["new"]:
            raise serializers.ValidationError(
                "Las nueva contraseña debe ser distinta a la anterior"
            )
        return attrs
