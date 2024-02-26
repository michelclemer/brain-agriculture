from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from src.apps.region.api.serializers import (CitySerializer, CountrySerializer,
                                             StateSerializer)
from src.apps.region.models import CityModel, CountryModel, StateModel


class CityViewSet(ModelViewSet):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer
    http_method_names = ["get"]
    filter_backends = [DjangoFilterBackend]


class StateViewSet(ModelViewSet):
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer
    http_method_names = ["get"]
    filter_backends = [DjangoFilterBackend]


class CountryViewSet(ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
    http_method_names = ["get"]
    filter_backends = [DjangoFilterBackend]


