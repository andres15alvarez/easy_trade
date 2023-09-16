from rest_framework import serializers

from easy_trade.catalog.models import City, Country, Document, Gender, State, UserType


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = ["country"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ["state"]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = "__all__"
