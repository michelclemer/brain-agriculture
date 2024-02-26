from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from src.apps.agriculture.api.serializers import (AgricultureListSerializer,
                                                  AgricultureSerializer,
                                                  PlantedCropsSerializer)
from src.apps.agriculture.models import AgricultureModel, PlantedCropsModel


class AgriculteViewSet(ModelViewSet):
    queryset = AgricultureModel.objects.all()
    serializer_class = AgricultureSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]

    def list(self, request, *args, **kwargs):
        self.serializer_class = AgricultureListSerializer
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = AgricultureListSerializer
        return super().update(request, *args, **kwargs)


class PlantedCropsViewSet(ModelViewSet):
    queryset = PlantedCropsModel.objects.all()
    serializer_class = PlantedCropsSerializer
    http_method_names = ["get"]
    filter_backends = [DjangoFilterBackend]
