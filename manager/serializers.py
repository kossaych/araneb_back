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











from rest_framework import serializers
from .models import*
class AccouplementSerializer(serializers.ModelSerializer):
    class Meta :
        model=Accouplement
        fields=['mère','père','date_acouplage']
class GroupeProductionSerializer(serializers.ModelSerializer):
    class Meta :
        model=GroupeProduction
        fields=[
        "date_naissance",
        "nb_lapins_nées",
        "nb_lapins_mortes_naissances",
         ]
class LapinProductionSerializer(serializers.ModelSerializer):
    class Meta :
        model=LapinProduction
        fields=["id",'groupe','race','state','cage','date_mort','prix','date_vent']               