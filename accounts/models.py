from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Race(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    race=models.CharField(max_length=200,default='------')
    Moyenne_poid_malle=models.IntegerField(default=3500)
    Moyenne_poid_femalle=models.IntegerField(default=3000)
    Moyenne_production_annuelle=models.IntegerField(default=50)
    Moyenne_poid_2moi=models.IntegerField(default=3500)
    Moyenne_production_par_accouplement=models.IntegerField(default=50)
    def __str__(self):
         return self.race
class Maladie(models.Model):
    TYPES_MALADIES_LAPINS=[   
                        ("Les_maladies_dermatologiques","Les maladies dermatologiques"),
                        ("Les_maladies_respiratoires","Les maladies respiratoires"),
                        ("Les_maladies_digestives","Les maladies digestives"),
                        ("Les_maladies_de_l'appareil_urinaire","Les maladies de l'appareil urinaire"),
                        ("La_maladie_hémorragique_du_lapin","La maladie hémorragique du lapin"),
                        ("Les_tumeurs","Les tumeurs"),
    ]
    maladie=models.CharField(max_length=200,default='____')
    type=models.CharField(choices=TYPES_MALADIES_LAPINS,max_length=200,default='__')
    def __str__(self):
        return str(self.maladie)
class GeneralConfig(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    DEVISE_LIST=(('din tun','din tun'),('din alg','din alg'))
    unité_poids=models.CharField(choices=(('kg','kg'),('g','g')),max_length=200,default='g')
    date_souvrage_aprés=models.IntegerField(default=25)
    unité_devise=models.CharField(choices=DEVISE_LIST,max_length=200,default='din tun')
    nb_production_naturel=models.IntegerField(default=8)
    nb_mortalité_naturel=models.IntegerField(default=2)
    consomation_naturel=models.IntegerField(default=7500)
    coup_alimentation=models.IntegerField(default=1)

class CodeVirif(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=8, null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now())
    is_valid=models.BooleanField(default=True)

class Profil(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=8, null=True,blank=True)
    address=models.CharField(max_length=100, null=True,blank=True)
@receiver(post_save,sender=User)
def add_profil_and_token(sender,instance,created,**kwargs):
        if created:
            Profil.objects.create(
                                    user=instance
                                )
            Token.objects.create(
                                    user=instance
                                )  
            GeneralConfig.objects.create(
                                    user=instance
                                )  
            Race.objects.create(
                                    user=instance,
                                    race='Gaint Flander' 
                                )
            Race.objects.create(
                                    user=instance,
                                    race='Flemish Giant' 
                                )
            Race.objects.create(
                                    user=instance,
                                    race='Chinchilla' 
                                )
            Race.objects.create(
                                    user=instance,
                                    race='New Zealand White' 
                                )
            Race.objects.create(
                                    user=instance,
                                    race='California' 
                                )
            Race.objects.create(
                                    user=instance,
                                    race='Rex' 
                                )
                                
