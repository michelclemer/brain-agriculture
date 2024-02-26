from django.db import models


class AgricultureModel(models.Model):
    agr_id = models.BigAutoField(primary_key=True)
    agr_productor_name = models.CharField(max_length=500)
    agr_farm_name = models.CharField(max_length=500)
    agr_cnpf = models.CharField(max_length=20, null=True)
    agr_cnpj = models.CharField(max_length=20, null=True)
    agr_total_area_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    agr_arable_are_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    agr_vegetable_area_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    city_id = models.ForeignKey(
        "region.CityModel",
        on_delete=models.CASCADE,
        db_column="city_id",
        related_name="agr_id_city_id"
    )

    class Meta:
        db_table = "agricultura"

    def __str__(self):
        return self.agr_total_area_hectares + " - " + self.agr_arable_are_hectares + " - " + self.agr_vegetable_area_hectares


class PlantedCropsModel(models.Model):
    pcr_id = models.BigAutoField(primary_key=True)
    pcr_label = models.CharField(max_length=100)

    class Meta:
        db_table = "colheita_plantada"

    def __str__(self):
        return self.pcr_label


class PlantedCropsAgriModel(models.Model):
    pca_id = models.BigAutoField(primary_key=True)
    agri_id = models.ForeignKey(
        AgricultureModel,
        on_delete=models.CASCADE,
        related_name="pca_id_agri_id"
    )
    pcr_id = models.ForeignKey(
        PlantedCropsModel,
        on_delete=models.CASCADE,
        related_name="pca_id_pcr_id"
    )

    class Meta:
        db_table = "agricultura_colheita_plantada"

    def __str__(self):
        return self.agri_id + " - " + self.pcr_id
