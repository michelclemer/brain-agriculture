from rest_framework import serializers

from src.apps.region.models import CityModel, CountryModel, StateModel


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        fields = "__all__"

