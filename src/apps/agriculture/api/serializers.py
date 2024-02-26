from rest_framework import serializers

from src.apps.agriculture.models import (AgricultureModel,
                                         PlantedCropsAgriModel,
                                         PlantedCropsModel)
from src.apps.region.api.serializers import CitySerializer
from src.utils.validate_fields.validate_cpf_cnpj import validate_cpf_cnpj


class AgricultureListSerializer(serializers.ModelSerializer):
    city_id = serializers.SerializerMethodField()
    pcr_list = serializers.SerializerMethodField()

    class Meta:
        model = AgricultureModel
        fields = "__all__"

    def get_city_id(self, obj: AgricultureModel):
        return CitySerializer(obj.city_id).data

    def get_pcr_list(self, obj: AgricultureModel):
        return PlantedCropsAgriSerializer(obj.pca_id_agri_id.all(), many=True).data


class AgricultureSerializer(serializers.ModelSerializer):
    pcr_list = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = AgricultureModel
        fields = "__all__"

    def validate(self, attrs):
        if attrs.get('agr_arable_are_hectares') + attrs.get('agr_vegetable_area_hectares') > attrs.get('agr_total_area_hectares'):
            raise serializers.ValidationError("A soma das áreas não pode exceder a área total da fazenda.")
        if attrs.get("agr_cnpf") and not validate_cpf_cnpj(attrs.get("agr_cnpf"), "cpf"):
            raise serializers.ValidationError({"agr_cnpf": "CPF inválido."})
        if attrs.get("agr_cnpj") and not validate_cpf_cnpj(attrs.get("agr_cnpj"), "cnpj"):
            raise serializers.ValidationError({"agr_cnpj": "CNPJ inválido."})
        return super().validate(attrs)

    def create(self, validated_data):
        list_pcr = validated_data.pop("pcr_list", [])
        result = super().create(validated_data)
        if list_pcr:
            for pcr_id in list_pcr:
                try:
                    PlantedCropsAgriModel.objects.create(
                        agri_id=result,
                        pcr_id=PlantedCropsModel.objects.get(pcr_id=pcr_id)
                    )
                except PlantedCropsModel.DoesNotExist:
                    raise serializers.ValidationError({"pcr_list": "Colheita Não Encontrada."})

        return result


class PlantedCropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedCropsModel
        fields = "__all__"


class PlantedCropsAgriSerializer(serializers.ModelSerializer):
    pcr_id = serializers.SerializerMethodField()

    class Meta:
        model = PlantedCropsAgriModel
        fields = "__all__"

    def get_pcr_id(self, obj: PlantedCropsAgriModel):
        return PlantedCropsSerializer(obj.pcr_id).data
