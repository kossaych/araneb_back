from rest_framework import serializers
from .models import*
class MalleSerializer(serializers.ModelSerializer):
    class Meta :
        model=Malle
        fields=("race","date_naissance","cage","img",)
class FemalleSerializer(serializers.ModelSerializer):
    class Meta :
        model=Femalle
        fields=[
                "id",
                "race",
                "date_naissance",
                "cage",
                "date_mort",
                "prix",
                "date_vent",
         ]
class PoidMalleSerializer(serializers.ModelSerializer):
    class Meta :
        model=Malle
        fields='__all__'
class PoidFemalleSerializer(serializers.ModelSerializer):
    class Meta :
        model=Femalle
        fields='__all__'