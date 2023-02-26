from django import forms
from .models import*
class MalleForm(forms.ModelForm):
    class Meta :
        model= Malle
        fields=['date_naissance','cage']
        widgets={
            'date_naissance':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                       'id':'dateNaissanceInput',
                       'type': 'date'  ,
                       
                      }),

            

        }
class FemalleForm(forms.ModelForm):
    class Meta :
        model= Femalle
        fields=['date_naissance','cage']
        widgets={
      
            'date_naissance':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                       'id':'dateNaissanceInput',
                       'type': 'date',
                         
                      }),
            
            
           

        }       
class FemalleMorte(forms.ModelForm):
    class Meta :
        model= Femalle
        fields=['date_mort']
        widgets={
      
            'date_mort':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                       
                       'type': 'date'  
                      }),
            

        }               
class MalleMorte(forms.ModelForm):
    class Meta :
        model= Malle
        fields=['date_mort']
        widgets={
      
            'date_mort':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                       
                       'type': 'date'  
                      }),
            

        }                       
                       
class MalleVendue(forms.ModelForm):
    class Meta :
        model= Malle
        fields=['date_vent','prix']
        widgets={
            'prix':forms.NumberInput(attrs={'class': ' btn bg-light bg-opacity-25 ', 
                       
                         
                      }),
            'date_vent':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                    
                       'type': 'date'  
                      }),
            

        }
class FemalleVendue(forms.ModelForm):
    class Meta :
        model= Femalle
        fields=['date_vent','prix']
        widgets={
            'prix':forms.NumberInput(attrs={'class': ' btn bg-light bg-opacity-25 ', 
                       
                         
                      }),
            'date_vent':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': ' btn bg-light bg-opacity-25  ', 
                    
                       'type': 'date'  
                      }),
            

        }        