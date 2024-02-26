
from django.db import models


class CountryModel(models.Model):
    pai_id = models.BigAutoField(primary_key=True)
    pai_nome = models.CharField(max_length=60)
    pai_nome_pt = models.CharField(max_length=60)
    pai_sigla = models.CharField(max_length=2, null=True)
    pai_bacen = models.IntegerField()

    class Meta:
        db_table = 'pais'

    def __str__(self):
        return self.pai_nome


class StateModel(models.Model):
    std_id = models.BigAutoField(primary_key=True)
    std_nome = models.CharField(max_length=60)
    std_uf = models.CharField(max_length=2)
    std_ibge = models.IntegerField()
    pai_id = models.ForeignKey(
        CountryModel,
        on_delete=models.CASCADE,
        db_column='pai_id',
        null=True
    )
    std_ddd = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        return self.std_nome


class CityModel(models.Model):
    city_id = models.BigAutoField(primary_key=True)
    city_nome = models.CharField(max_length=120)
    std_id = models.ForeignKey(StateModel, on_delete=models.CASCADE, db_column='std_id', null=True)
    city_ibge = models.IntegerField(null=True)
    city_lat_lon = models.CharField(max_length=500, null=True)
    city_latitude = models.FloatField(null=True)
    city_longitude = models.FloatField(null=True)
    city_cod_tom = models.SmallIntegerField(default=0, null=True)

    class Meta:
        db_table = 'cidade'

    def __str__(self):
        return self.city_nome
