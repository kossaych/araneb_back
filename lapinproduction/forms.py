from .models import*
from django import forms
class GroupeProductionForm(forms.ModelForm):
      class Meta :
            model=GroupeProduction 
            fields=[
            'date_naissance',
            'nb_lapins_nées',
            'nb_lapins_mortes_naissances',
            ]
            widgets={
            'date_naissance':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                       'id':'dateNaissanceInput',
                       'type':'date'  
                      }),        
            'nb_lapins_nées':forms.NumberInput(
                attrs={'class': ' btn bg-light bg-opacity-25 ', 
                       'id':'nbLapinsNées',
                         
                      }),
            'nb_lapins_mortes_naissances':forms.NumberInput(
                attrs={'class': ' btn bg-light bg-opacity-25 ', 
                       'id':'nbLapinsMortesNaissances',
                         
                      }),
        }
class AccouplementForm(forms.ModelForm):
      class Meta :
            model=Accouplement
            fields=[    
            'date_acouplage',                  
            ]
            
            widgets={
            'date_acouplage':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                       'id':'dateAcouplageInput',
                       'type':'date'  
                      }),        
        }
class LapinProductionForm(forms.ModelForm):
      class Meta :
            model=LapinProduction
            fields=[
            'sex',
            ]