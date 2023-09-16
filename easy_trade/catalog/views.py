from rest_framework import generics, status
from rest_framework.response import Response

from easy_trade.catalog.models import City, Country, Document, Gender, State, UserType
from easy_trade.catalog.serializers import (
    CitySerializer,
    CountrySerializer,
    DocumentSerializer,
    GenderSerializer,
    StateSerializer,
    UserTypeSerializer,
)


class CountryView(generics.ListAPIView):
    def list(self, request):
        queryset = Country.objects.filter()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StateView(generics.ListAPIView):
    def list(self, request):
        country_id = request.query_params.get("country")
        queryset = State.objects.filter(country_id=country_id)
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityView(generics.ListAPIView):
    def list(self, request):
        state_id = request.query_params.get("state")
        queryset = City.objects.filter(state_id=state_id)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DocumentView(generics.ListAPIView):
    def list(self, request):
        queryset = Document.objects.filter()
        serializer = DocumentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenderView(generics.ListAPIView):
    def list(self, request):
        queryset = Gender.objects.filter()
        serializer = GenderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserTypeView(generics.ListAPIView):
    def list(self, request):
        queryset = UserType.objects.filter()
        serializer = UserTypeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
