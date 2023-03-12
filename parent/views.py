from email.policy import HTTP
from lapinproduction.models import*
from accounts.models import*
from django.shortcuts import redirect, render
from .models import*
from .forms import *
from .serializers import*
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
aujourdhui_date=str(timezone.now().year)+"-"+str(timezone.now().month)+'-'+str(timezone.now().day)
# calculer l'age d'un lapin retourner le nombre de jour a partir du date de naissance (str!!) il retourne un entier
def age(naissance):
        """         naissance=str(naissance)
        année_naissance =int(naissance[:naissance.index('-')])
        moi_naissance =int(naissance[naissance.index('-')+1:naissance.index('-',naissance.index('-')+1)])
        jour =int(naissance[naissance.index('-',naissance.index('-',naissance.index('-')+1))+1:])
        today = timezone.now() 
        nb_mois=today.month-moi_naissance # nombre des mois
        jours_moi=0 # le nombre des jours correspondant au nombre des mois
        if nb_mois>0:
            for moi in range(moi_naissance,today.month):
                if moi in [1,3,5,7,8,10,12]:
                    jours_moi=jours_moi+31
                elif moi in [4,6,5,9,8,10,11]  :
                    jours_moi=jours_moi+30
                else:    
                    if (année_naissance%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if année_naissance%400==0:
                                jours_moi=jours_moi+29
                            else:
                                jours_moi=jours_moi+28
                    else:
                            if année_naissance%4==0:
                                jours_moi=jours_moi+29
                            else:
                                jours_moi=jours_moi+28
        elif nb_mois<0:
            for moi in range(moi_naissance,today.month,-1):
                if moi in [1,3,5,7,8,10,12]:
                    jours_moi=jours_moi-31
                elif moi in [4,6,5,9,8,10,11]  :
                    jours_moi=jours_moi-30
                else :
                    if (année_naissance%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                        if année_naissance%400==0:
                            jours_moi=jours_moi-29
                        else:
                            jours_moi=jours_moi-28
                    else:
                        if année_naissance%4==0:
                            jours_moi=jours_moi-29
                        else:
                            jours_moi=jours_moi-28
        nb_anné=today.year-année_naissance  # nombre des annés
        jours_anné=0 # le nombre des  jours correspondant au nombre des annés
        if nb_anné>0:
            for année in range(année_naissance,today.year):
                    if (année%1000)%100==0:  # si le disaine et l'unité de nobre de l'anné est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier année bissextile qabissa)
                        if année%400==0:
                            jours_anné=jours_anné+366
                        else:
                            jours_anné=jours_anné+365
                    else:
                        if année%4==0:
                            jours_anné=jours_anné+366
                        else:
                            jours_anné=jours_anné+365
        elif nb_anné<0:
            for année in range(année_naissance,today.year,-1):
                    if (année%1000)%100==0:  # si le disaine et l'unité de nobre de l'anné est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier année bissextile qabissa)
                        if année%400==0:
                            jours_anné=jours_anné-366
                        else:
                            jours_anné=jours_anné-365
                    else:
                        if année%4==0:
                            jours_anné=jours_anné-366
                        else:
                            jours_anné=jours_anné-365 
        age = jours_anné+jours_moi+ (today.day - jour)
        return  age """
        str_d1 =str(naissance)
        aujourdhui_date=str(date.today())
        try :
            d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        except:
            d1 = str_d1
        d2 = datetime.strptime(aujourdhui_date, "%Y-%m-%d")
        age = str(d2 - d1)
        try :    
            age=int(age[:age.index('d')])
        except:
            age=0
        return  age
# retourner l'age en anné mois et jours sous forme str a partir de l'age en jour
def age_handler(age):
        today=timezone.now()
        if age >=0:
            #for an in range(today.year-(age//365),today.year):
            nb_anné=0
            while (age>=365):
                if (today.year-nb_anné%1000)%100==0:  # si le disaine et l'unité de nobre de l'anné est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier année bissextile qabissa)
                    if today.year-nb_anné%400==0:
                        age-=366
                    else:
                        age-=365
                else:
                    if today.year-nb_anné%4==0:
                        age-=366
                    else:
                        age-=365
                nb_anné+=1        
            nb_mois=0
            while (age>=30):
                if today.month-nb_mois in [1,3,5,7,8,10,12]:
                    age-=31
                elif today.month-nb_mois in [4,6,5,9,8,10,11]  :
                    age-=30
                else:    
                    if (today.year-nb_anné%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if today.year-nb_anné %400==0:
                                age-=29
                            else:
                                age-=28
                    else:
                            if today.year-nb_anné %4==0:
                                age-=29
                            else:
                                age-=28
                nb_mois+=1        
            
        return str(nb_anné)+" ans "+str(nb_mois)+" mois "+str(age)+" jours "  

#######################////////////// les statistiques de production ////////////////////////########################    
    # en ajoutant f , m ou rp a la fin de ces noms pour dit que ces calcule sont fais pour une categorie f : categorie des lapine m:categorie des malles et rp : categorie des lapin race pure 'californiaire'
# return le dernier groupe de production produit par une femalle (si elle n'a pas des groupe retourner False)
def dernier_groupe_production(id_mère):
            date=" "
            dernier_groupe={}
            for groupe in GroupeProduction.objects.all():
                if groupe.acouplement.mère.id==id_mère:
                        if date==" ":
                            date=groupe.date_naissance
                            dernier_groupe=groupe
                        elif age(groupe.date_naissance)<age(date):
                            date=groupe.date_naissance
                            dernier_groupe=groupe
            if dernier_groupe=={}:
                return False # False sig que la femalle n"a pas encore des groupe
            else :
                return dernier_groupe  
# totale de production des lapin par une femalle dernière naissance
def TP(id_mère):
    if dernier_groupe_production(id_mère)==False:
        return 0
    else :
        return dernier_groupe_production(id_mère).nb_lapins_nées                                  
# totale de mortalité des lapin de production a la naissance  d'une femalle a la derniere naissance
def TMN(id_mère):
        if dernier_groupe_production(id_mère)==False:
            return 0
        else :
            return dernier_groupe_production(id_mère).nb_lapins_mortes_naissances
# totale de mortalité des lapin de production d'une femalle a la derniere naissance
def TM(id_mère):
            nb=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe==dernier_groupe_production(id_mère) and lapin.state=="mort":
                        nb=nb+1
            return nb
# totale  des lapin de production non morte d'une femalle a la derniere naissance
def TPnet(id_mère):
            nb=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe==dernier_groupe_production(id_mère) and lapin.state=="production":
                        nb=nb+1
            return nb      
#m ou f pour les statistique des malles ou des femalles 
def TPm(id_mère):
            if dernier_groupe_production(id_mère)==False:
                return 0
            else :
                nb=0
                for lapin in LapinProduction.objects.all():
                    if lapin.groupe == dernier_groupe_production(id_mère) and lapin.sex=='malle':
                            nb=nb+1
                return nb
def TMm(id_mère):
            if dernier_groupe_production(id_mère)==False:
                return 0
            else :
                nb=0
                for lapin in LapinProduction.objects.all():
                    if lapin.groupe == dernier_groupe_production(id_mère) and lapin.sex=='malle' and lapin.state=="mort":
                            nb=nb+1
                return nb
def TPnetm(idparent):
            return TPm(idparent)-TMm(idparent)
def TPf(id_mère):
            if dernier_groupe_production(id_mère)==False:
                return 0
            else :
                nb=0
                for lapin in LapinProduction.objects.all():
                    if lapin.groupe == dernier_groupe_production(id_mère) and lapin.sex=='femalle':
                            nb=nb+1
                return nb
def TMf(id_mère):
            if dernier_groupe_production(id_mère)==False:
                return 0
            else :
                nb=0
                for lapin in LapinProduction.objects.all():
                    if lapin.groupe == dernier_groupe_production(id_mère) and lapin.sex=='femalle' and lapin.state=="mort":
                            nb=nb+1
                return nb
def TPnetf(idparent):
            return TPf(idparent)-TMf(idparent)
##***************************************************************************(
# rp pour les statistique d'une race indiqué  !! le paramètre races doit etre une liste
def TPrp(id_mère,races):
            nb=0
            for groupe in GroupeProduction.objects.all():
                
                if id_mère==groupe.acouplement.mère.id :
                    for lapin in LapinProduction.objects.all():
                        
                        if lapin.groupe.id == groupe.id  and lapin.race in races:
                            nb=nb+1
            return nb         
def TMrp(id_mère,races):
            nb=0
            for groupe in GroupeProduction.objects.all():                    
                    if id_mère==groupe.acouplement.mère.id :
                            for lapin in LapinProduction.objects.all():
                                        
                                        if lapin.groupe.id == groupe.id  and lapin.state=='mort' and lapin.race in races:
                                            nb=nb+1
            return nb
def TPnetrp(id_mère,races):
            return TPrp(id_mère,races)-TMrp(id_mère,races)
#*********************************************************************)


###################////////// les statistiques des vent //////////////////###########
# return le nombre des lapins vendues  pandant ce mois
def TV(idparent):
            nb=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe.acouplement.mère.id == idparent  and lapin.state=='vendue':
                    if str(lapin.date_vent).find('-')!=(-1):
                        if age(str(lapin.date_vent))<= 32 :
                            nb=nb+1
            return nb   
#return le nombre des lapins malles vendues  pandant ce mois
def TVm(idparent):
            nb=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe.acouplement.mère.id == idparent  and lapin.state=='vendue':
                    if lapin.sex=="malle":
                        if str(lapin.date_vent).find('-')!=(-1):
                            if age(str(lapin.date_vent))<= 32 :
                                nb=nb+1
            return nb   
#return le nombre des lapins femalles vendues  pandant ce mois
def TVf(idparent):
            nb=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe.acouplement.mère.id == idparent  and lapin.state=='vendue':
                    if lapin.sex=="femalle":
                        if str(lapin.date_vent).find('-')!=(-1):
                            if age(str(lapin.date_vent))<= 32 :
                                nb=nb+1
            return nb   
#return le plus grands prix dans les prix des lapins vendues  pandant ce mois
def grandprix(idparent):
            max=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe.acouplement.mère.id == idparent  and lapin.state=='vendue':
                        if str(lapin.date_vent).find('-')!=(-1):
                            if age(str(lapin.date_vent))<= 32 :
                                if lapin.prix > max:
                                    max=lapin.prix
            return max
#return le plus bas prix dans les prix des lapins vendues  pandant ce mois
def basprix(idparent):
            min=10000000000
            for lapin in LapinProduction.objects.all():
                if lapin.groupe.acouplement.mère.id == idparent  and lapin.state=='vendue':
                        if str(lapin.date_vent).find('-')!=(-1):
                            if age(str(lapin.date_vent))<= 32 :  
                                if lapin.prix < min:
                                    min=lapin.prix
            if min==10000000000:
                return 0                        
            return min            
##return le totale des prix dans les prix des lapins vendues  pandant ce mois
def totaleprix(idparent):
            totale=0
            for lapin in LapinProduction.objects.all():
                if lapin.groupe.acouplement.mère.id == idparent  and lapin.state=='vendue':
                        if str(lapin.date_vent).find('-')!=(-1):
                            if age(str(lapin.date_vent))<= 32 :
                                totale=totale+lapin.prix
            return totale 
##return le moyenne des prix prix dans les prix des lapins vendues  pandant ce mois
def moyprix(idparent):
    if TV(idparent!=0):
           return totaleprix(idparent)/TV(idparent) 
    return 0                        
################################################################################


############//////// les statistiques des poids ///////////////###########################
# retourner la dernier date de mesure des poids d'un groupe de production
def date_dernier_mesure(id_groupe):
            date=""
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe.id==id_groupe:
                        if date=="":
                            date=poid.date_mesure
                        elif age(poid.date_mesure)<age(date):
                            date=poid.date_mesure
            return date 
# moyenne des poids du dernière groupe du production a la naissance
def MPN(id_mère):
            totale_poids=0
            nblapins=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_naissance:
                                    nblapins+=1
                                    totale_poids=totale_poids+poid.valeur
            moy=0
            if nblapins != 0 :
                moy=totale_poids/nblapins
            return moy           
# le plus grand poid des poids du dernière groupe du production a la naissance
def TOPPN(id_mère):
            max=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_naissance:
                        if poid.valeur > max:
                            max=poid.valeur
            return max  
## le plus bas poid des poids du dernière groupe du production a la naissance
def BASPN(id_mère):
            min=99999
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_naissance:
                        if poid.valeur < min:
                            min=poid.valeur
            return min      

# moyenne des poids du dernière groupe de production la dernière mesure
def MPDM(id_mère):
            totale_poids=0
            nblapins=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==date_dernier_mesure(poid.lapin.groupe):
                                    nblapins+=1
                                    totale_poids=totale_poids+poid.valeur
            moy=0
            if nblapins != 0 :
                moy=totale_poids/nblapins
            return moy       
# le plus grand poid des poids du dernière groupe du production la dernière mesure
def TOPPDM(id_mère):
            max=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_dernier_mesure(poid.lapin.groupe):
                        if poid.valeur > max:
                            max=poid.valeur
            return max  
## le plus bas poid des poids du dernière groupe du production la dernière mesure
def BASPDM(id_mère):
            min=99999
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_dernier_mesure(poid.lapin.groupe):
                        if poid.valeur < min:
                            min=poid.valeur
            return min      

# moyenne des poids du dernière groupe du production au sevrage
def MPS(id_mère):
            totale_poids=0
            nblapins=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_souvrage:
                                    nblapins+=1
                                    totale_poids=totale_poids+poid.valeur
            moy=0
            if nblapins != 0 :
                moy=totale_poids/nblapins
            return moy  
# le plus grand poid des poids du dernière groupe du production au sevrage
def TOPPS(id_mère):
            max=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_souvrage:
                        if poid.valeur > max:
                            max=poid.valeur
            return max         
## le plus bas poid des poids du dernière groupe du production au sevrage
def BASPS(id_mère):
            min=99999
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe==dernier_groupe_production(id_mère):
                    if poid.date_mesure==poid.lapin.groupe.date_souvrage:
                        if poid.valeur < min:
                            min=poid.valeur
            return min      
##################################################################################################
################# consomation ################################
# le totale de consomation d'une femalle dans les 30 dernière jours
def Cons(idparent):
            totale=0
            for cons in ConsFemalle.objects.all():
                if cons.femalle.id == idparent:
                    if age(str(cons.date_mesure))<=32:
                        totale=totale+cons.valeur
            return totale
#################################################################################################
# retourner True si la femalle est nourice dans un jour précie sinon False
def nourice(id_mère,date_jour) :  
    for groupe in GroupeProduction.objects.all():
        if groupe.acouplement.mère.id==id_mère:
            if groupe.date_souvrage ==None:
                if age(groupe.date_naissance)-age(date_jour)>=0: # le calcule basé sur la diférence des jour entre le date de naissance et le date précie 
                    return True
            else :
                if age(groupe.date_souvrage)-age(date_jour)<0 and age(groupe.date_naissance)-age(date_jour)>=0: # le calcule basé sur la diférence des jour entre le date de naissance et le date précie     
                    return True

    return False
#retourner True si la femalle est enciente dans un jour précie sinon False
def enceinte(id_mère,date_jour):
    if age(date_jour)>=0: # pour virifier que le date est passé
        for acouplement in Accouplement.objects.filter(mère=id_mère):
            if 33>=age(str(acouplement.date_acouplage))-age(str(date_jour))>=0: # la différence entre l'age du date d'acouplage et l'age du date cherché doit etre positive et inferieur a 33 pour indiquer que le date demander et dans le plage (range) d'accouplement
                if acouplement.test=="non_vérifié" or acouplement.test=="enciente": # pour assurer que la femalle est effectivement enciente   
                    if acouplement.state== "avant_naissance"  :
                        return True
                    else:    
                        if age(GroupeProduction.objects.get(acouplement=acouplement).date_naissance)-age(str(date_jour))<0: # pour assurer que la fonction return True meme si l'acouplement est déja aprés la naissance (et ca se fait avec une verificatinon par le date de naissance le date demander doit etre avant la date de naissance)
                            return True
                else :
                    if age(str(date_jour))>=age(str(acouplement.date_test)):
                        return True        

        return False
    return False    
# retourner le date de naissance a partir d'un age par jour
def age_revers(age_jours):
        if age_jours >= 364 :
            for an in range((timezone.now().year-(age_jours//365))-1,(timezone.now().year-(age_jours//365))+1):
                for moi in range(1,13):                       
                                if moi in [4,6,9,11]:
                                                for jour in range(1,31):
                                                    if age(str(an)+"-"+str(moi)+"-"+str(jour)) == age_jours:
                                                        date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                        if len(str(moi))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(moi))==1:
                                                                date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                        
                                                        return date                                                
                                elif moi in [1,3,5,7,8,10,12]:   
                                                for jour in range(1,32):
                                                    if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                        if len(str(moi))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(moi))==1:
                                                                date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                        
                                                        return date                                                                              
                                if moi == 2 :
                                    if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                            if an%400==0:
                                                for jour in range(1,30):

                                                    if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                        if len(str(moi))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(moi))==1:
                                                                date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                        
                                                        return date                                              
                                            else:
                                                for jour in range(1,29):

                                                    if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                        if len(str(moi))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(moi))==1:
                                                                date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                        
                                                        return date                                               
                                    else:
                                            if an%4==0:
                                                for jour in range(1,30):

                                                    if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                        if len(str(moi))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(moi))==1:
                                                                date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                        
                                                        return date                                            
                                            else:
                                                for jour in range(1,29):

                                                    if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                        if len(str(moi))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(moi))==1:
                                                                date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                        
                                                        return date                                     
        else:      
            if (int(age(str(timezone.now().year)+"-01-01"))>=age_jours):#pour assurer que les dates doit  etre dans cette anné
                    an = timezone.now().year   
            else:
                    an = timezone.now().year-1                   
            for moi in range(1,13):                       
                            if moi in [4,6,9,11]:
                                            for jour in range(1,31):
                                                if age(str(an)+"-"+str(moi)+"-"+str(jour)) == age_jours:
                                                    date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                    if len(str(moi))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(moi))==1:
                                                            date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                    
                                                    return date                                                
                            elif moi in [1,3,5,7,8,10,12]:   
                                            for jour in range(1,32):
                                                if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                    if len(str(moi))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(moi))==1:
                                                            date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                    
                                                    return date                                                                              
                            if moi == 2 :
                                if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                        if an%400==0:
                                            for jour in range(1,30):

                                                if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                    if len(str(moi))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(moi))==1:
                                                            date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                    
                                                    return date                                              
                                        else:
                                            for jour in range(1,29):

                                                if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                    if len(str(moi))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(moi))==1:
                                                            date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                    
                                                    return date                                               
                                else:
                                        if an%4==0:
                                            for jour in range(1,30):

                                                if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                    if len(str(moi))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(moi))==1:
                                                            date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                    
                                                    return date                                            
                                        else:
                                            for jour in range(1,29):

                                                if age(str(an)+"-"+str(moi)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(moi)+"-"+str(jour)
                                                    if len(str(moi))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(moi)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(moi))==1:
                                                            date=str(an)+"-0"+str(moi)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(moi)+"-0"+str(jour)
                                                    
                                                    return date                                     
# retourner une liste contenant les dates succésivement a partir du intial_date jusqu'a final_date
def list_dates(initial_date,final_date):
    année_initial_date =(initial_date[:initial_date.index('-')])
    année_final_date =(final_date[:final_date.index('-')])
    moi_initial_date =(initial_date[initial_date.index('-')+1:initial_date.index('-',initial_date.index('-')+1)])
    jour_initial_date =(initial_date[initial_date.index('-',initial_date.index('-',initial_date.index('-')+1))+1:])
    moi_final_date =(final_date[final_date.index('-')+1:final_date.index('-',final_date.index('-')+1)])
    jour_final_date =(final_date[final_date.index('-',final_date.index('-',final_date.index('-')+1))+1:])
    # pour garantir que les dates de debut et de fin sont en bonne forme  
    if len(moi_initial_date)==1 and len(jour_initial_date)==1:
        initial_date=année_initial_date+"-0"+moi_initial_date+"-0"+jour_initial_date
    else:    
        if len(moi_initial_date)==1:
            initial_date=année_initial_date+"-0"+moi_initial_date+"-"+jour_initial_date
        if len(jour_initial_date)==1:
            initial_date=année_initial_date+"-"+moi_initial_date+"-0"+jour_initial_date
    
    if len(moi_final_date)==1 and len(jour_final_date)==1:
        final_date=année_final_date+"-0"+moi_final_date+"-0"+jour_final_date
    else:    
        if len(moi_final_date)==1:
            final_date=année_final_date+"-0"+moi_final_date+"-"+jour_final_date
        if len(jour_final_date)==1:
            final_date=année_final_date+"-"+moi_final_date+"-0"+jour_final_date
    
    
    list_dates=[]
    for an in range(int(initial_date[:initial_date.index('-')]),int(final_date[:final_date.index('-')])+1):
            for moi in range(1,13):
                if moi in [4,6,9,11]:
                                for jour in range(1,31):
                                    moi_date=str(moi)
                                    jour_date=str(jour)
                                    if moi in [4,6,9] and jour in [1,2,3,4,5,6,7,8,9]:
                                        moi_date="0"+str(moi)
                                        jour_date="0"+str(jour)
                                    else:
                                        if moi in [4,6,9]:
                                            moi_date="0"+str(moi)
                                        if jour in [1,2,3,4,5,6,7,8,9]:
                                            jour_date="0"+str(jour)
                                    date=str(an)+"-"+(moi_date)+"-"+(jour_date)
                                    list_dates.append(date)

                elif moi in [1,3,5,7,8,10,12]:
                                for jour in range(1,32):
                                    moi_date=str(moi)
                                    jour_date=str(jour)
                                    if moi in [1,3,5,7,8] and jour in [1,2,3,4,5,6,7,8,9]:
                                        moi_date="0"+str(moi)
                                        jour_date="0"+str(jour)
                                    else:
                                        if moi in [1,3,5,7,8]:
                                            moi_date="0"+str(moi)
                                        if jour in [1,2,3,4,5,6,7,8,9]:
                                            jour_date="0"+str(jour)
                                    date=str(an)+"-"+(moi_date)+"-"+(jour_date)
                                    list_dates.append(date)

                if moi == 2 :
                    if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if an %400==0:
                                for jour in range(1,30):
                                    moi_date=str(moi)
                                    jour_date=str(jour)
                                    if moi in [2] and jour in [1,2,3,4,5,6,7,8,9]:
                                        moi_date="0"+str(moi)
                                        jour_date="0"+str(jour)
                                    else:
                                        if moi in [2]:
                                            moi_date="0"+str(moi)
                                        if jour in [1,2,3,4,5,6,7,8,9]:
                                            jour_date="0"+str(jour)
                                    date=str(an)+"-"+(moi_date)+"-"+(jour_date)
                                    list_dates.append(date)

                            else:
                                for jour in range(1,29):
                                    moi_date=str(moi)
                                    jour_date=str(jour)
                                    if moi in [2] and jour in [1,2,3,4,5,6,7,8,9]:
                                        moi_date="0"+str(moi)
                                        jour_date="0"+str(jour)
                                    else:
                                        if moi in [2]:
                                            moi_date="0"+str(moi)
                                        if jour in [1,2,3,4,5,6,7,8,9]:
                                            jour_date="0"+str(jour)
                                    date=str(an)+"-"+(moi_date)+"-"+(jour_date)
                                    list_dates.append(date)

                    else:
                            if an %4==0:
                                for jour in range(1,30):
                                    moi_date=str(moi)
                                    jour_date=str(jour)
                                    if moi in [2] and jour in [1,2,3,4,5,6,7,8,9]:
                                        moi_date="0"+str(moi)
                                        jour_date="0"+str(jour)
                                    else:
                                        if moi in [2]:
                                            moi_date="0"+str(moi)
                                        if jour in [1,2,3,4,5,6,7,8,9]:
                                            jour_date="0"+str(jour)
                                    date=str(an)+"-"+(moi_date)+"-"+(jour_date)
                                    list_dates.append(date)

                            else:
                                for jour in range(1,29):
                                    moi_date=str(moi)
                                    jour_date=str(jour)
                                    if moi in [2] and jour in [1,2,3,4,5,6,7,8,9]:
                                        moi_date="0"+str(moi)
                                        jour_date="0"+str(jour)
                                    else:
                                        if moi in [2]:
                                            moi_date="0"+str(moi)
                                        if jour in [1,2,3,4,5,6,7,8,9]:
                                            jour_date="0"+str(jour)
                                    date=str(an)+"-"+(moi_date)+"-"+(jour_date)
                                    list_dates.append(date)
    return list_dates[list_dates.index(initial_date):list_dates.index(final_date)+1]
#retourner le totale de consomation pandent la periode de date initiale jusqu'a le date finale
def cons(id_mère,initial_date,final_date):
    cons=0
    if (age(final_date)-age(initial_date))<=0 and 90>=age(final_date)>=0:
        for jour in list_dates(initial_date,final_date):
            if  enceinte(id_mère,jour) and nourice(id_mère,jour) :
                cons=cons+500
            elif enceinte(id_mère,jour):
                cons=cons+250
            elif nourice(id_mère,jour) :
                cons=cons+300
            else:
                cons=cons+150
    return cons


def virif_cage(cage,user):
        for malle in Femalle.objects.filter(user=user):
                    if cage == int((malle.cage)[1:]):
                        return True
        return False 
def cage_vide (user):
        for i in range(1,len(Femalle.objects.filter(user=user))+1):
                if not virif_cage(i,user):
                    return 'F'+str(i)
        max=len(Femalle.objects.filter(user=user))
        return 'F'+str(max+1)
############## API----WIEWS ##################### 
class FemalleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virif_cage(self,cage):
        for malle in Femalle.objects.filter(user=self.request.user):
                    if cage == int((malle.cage)[1:]):
                        return True
        return False                
    def cage_vide (self):
        for i in range(1,len(Femalle.objects.filter(user=self.request.user))+1):
                if not self.virif_cage(i):
                    return 'F'+str(i)
        max=len(Femalle.objects.filter(user=self.request.user))
        return 'F'+str(max+1)
        # des fonctions du calcule pour calculer la prodectiviter d'une femalle
    def get(self,request):
        user=request.user
       
        femalles=[]
        femalles.clear() 
        for femalle in Femalle.objects.filter(user=user,state="production"):
                poids=[]
                for poid in PoidFemalle.objects.filter(femalle=femalle):
                    poids.append(
                        {
                            'femalle':str(poid.femalle),
                            'valeur':str(poid.valeur),
                            'date_mesure':str(poid.date_mesure),
                        })
               
                femalles.append({
                    'id':femalle.id,
                    "race":femalle.race,
                    "date_naissance":femalle.date_naissance,
                    "cage":femalle.cage,
                    "date_mort":femalle.date_mort,
                    "prix":femalle.prix,
                    "date_vent":femalle.date_vent,
                    "state":femalle.state,
                    'age':age_handler(age(str(femalle.date_naissance))),
                    'poid':poids,#liste des poids

                }
                )
                
        return Response(femalles,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=FemalleSerializer(data=request.data)
        if serializer.is_valid():
            if age(request.data["date_naissance"])>=120:
                user=request.user
                femalle=Femalle.objects.create(race=request.data["race"],date_naissance=request.data["date_naissance"],cage=self.cage_vide(),user=user)
                femalle.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response("la femalle que vous voulez ajouter a un age trés petit",status=status.HTTP_400_BAD_REQUEST)
        return Response("data not valid",status=status.HTTP_400_BAD_REQUEST)

class MalleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virif_cage(self,cage):
        for malle in Malle.objects.filter(user=self.request.user):
                    if cage == int((malle.cage)[1:]):
                        return True
        return False                
    def cage_vide (self):
        for i in range(1,len(Malle.objects.filter(user=self.request.user))+1):
                if not self.virif_cage(i):
                    return 'M'+str(i)
        max=len(Malle.objects.filter(user=self.request.user))
        return 'M'+str(max+1)
    def get(self,request):
        user=request.user
        malles=[]
        malles.clear()  
        for malle in Malle.objects.filter(user=user,state='production'):
                poids=[]
                for poid in PoidMalle.objects.filter(malle=malle):
                    poids.append(
                        {
                            'malle':str(poid.malle),
                            'valeur':str(poid.valeur),
                            'date_mesure':str(poid.date_mesure),
                        })
            
             
                malles.append(
                (
                {
                'id':malle.id,
                'img':str(malle.img),
                "race":malle.race,
                "date_naissance":malle.date_naissance,
                "cage":malle.cage,
                "date_mort":malle.date_mort,
                "prix":malle.prix,
                "date_vent":malle.date_vent,
                "state":malle.state,
                'age':age(str(malle.date_naissance)),
                'poid':poids,
                })
                )
                
        return Response(malles,status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer=MalleSerializer(data=request.data)
        if serializer.is_valid():
            if age(request.data["date_naissance"])>=120:
                user=request.user
                malle=Malle.objects.create(race=request.data["race"],date_naissance=request.data["date_naissance"],cage=self.cage_vide(),user=user)
                poids=[]
                for poid in PoidMalle.objects.filter(malle=malle):
                        poids.append(
                            {
                                'malle':str(poid.malle),
                                'valeur':str(poid.valeur),
                                'date_mesure':str(poid.date_mesure),
                            })
                malle={
                        'id':malle.id,
                        "race":malle.race,
                        "date_naissance":malle.date_naissance,
                        "cage":malle.cage,
                        "date_mort":malle.date_mort,
                        "prix":malle.prix,
                        "date_vent":malle.date_vent,
                        'state':malle.state,
                        'age':age(malle.date_naissance),
                        'poids':poids,
                        }  
                return Response(malle,status=status.HTTP_201_CREATED)
            return Response("le malle que vous voulez ajouter a un age trés petit",status=status.HTTP_400_BAD_REQUEST)    
        return Response('invalid data',status=status.HTTP_400_BAD_REQUEST)
class FemalleViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virif_femalle(self,id):
        for femalle in Femalle.objects.all():
            if femalle.id == id :
                return True
        return False    
    def put(self,request,id):
        if self.virif_femalle(id) :
            if  Femalle.objects.get(id=id).user==request.user:
                femalle=Femalle.objects.get(id=id)
                if age(str(femalle.create_at))==0:
                    if femalle.state=='production':
                        if age(request.data["date_naissance"])>=120:
                            femalle.date_naissance=request.data.get('date_naissance')
                            femalle.race=request.data.get("race")
                            femalle.date_naissance=request.data.get("date_naissance")
                            femalle.cage=request.data.get("cage")
                            femalle.date_mort=request.data.get("date_mort")
                            femalle.prix=request.data.get("prix")
                            femalle.date_vent=request.data.get("date_vent")
                            femalle.state=request.data.get('state')
                            femalle.save()
                            poids=[]
                            for poid in PoidFemalle.objects.filter(femalle=femalle):
                                poids.append(
                                            {
                                                'femalle':str(poid.femalle),
                                                'valeur':str(poid.valeur),
                                                'date_mesure':str(poid.date_mesure),
                                            })
                            femalle={
                                    'id':femalle.id,
                                    "race":femalle.race,
                                    "date_naissance":femalle.date_naissance,
                                    "cage":femalle.cage,
                                    "date_mort":femalle.date_mort,
                                    "prix":femalle.prix,
                                    "date_vent":femalle.date_vent,
                                    "state":femalle.state,
                                    'age':age(str(femalle.date_naissance)),
                                    'poid':poids,
                            }
                            return Response(femalle,status=status.HTTP_202_ACCEPTED)
                        else:return Response("invalid date",status=status.HTTP_400_BAD_REQUEST)  # l'age d'une mère doit etre super à 4 mois (120jours) 
                    else:return Response(status=status.HTTP_400_BAD_REQUEST) 
                else:return Response('tu peut pas changer les information d un malle apés '+str(age(str(femalle.create_at)))+"jour de son ajout",status=status.HTTP_400_BAD_REQUEST)           
            else:return Response(status=status.HTTP_401_UNAUTHORIZED)        
        else:return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        if self.virif_femalle(id) :
            if Femalle.objects.get(id=id).user==request.user:
                femalle=Femalle.objects.get(id=id)
                poids=[]
                for poid in PoidFemalle.objects.filter(femalle=femalle):
                    poids.append(
                                {
                                    'femalle':str(poid.femalle),
                                    'valeur':str(poid.valeur),
                                    'date_mesure':str(poid.date_mesure),
                                }
                                )              
                groupeprod=dernier_groupe_production(femalle.id)
                if (dernier_groupe_production(femalle.id)!=False):
                    groupeprod=dernier_groupe_production(femalle.id).id
                
                info={
            
                'TP':TP(femalle.id),
                'TM':TM(femalle.id),
                'TMN':TMN(femalle.id),
                'TPnet':TPnet(femalle.id),
                "dernière_groupe":groupeprod,
                
                #'TPf':TPf(femalle.id),
                #'TMf':TMf(femalle.id),
                #'TPnetf':TPnetf(femalle.id),

                #'TPm':TPm(femalle.id),
                #'TMm':TMm(femalle.id),
                #'TPnetm':TPnetm(femalle.id),
 
                "TV":TV(femalle.id),
                #"TVm":TVm(femalle.id),
                #"TVf":TVf(femalle.id),
                "totale_prix":totaleprix(femalle.id),
                "grand_prix":grandprix(femalle.id),
                "bas_prix":basprix(femalle.id),
                "moy_prix":moyprix(femalle.id),
                

                #"MPDM":MPDM(femalle.id),
                #"TOPPDM":TOPPDM(femalle.id),
                #"BASPDM":BASPDM(femalle.id),
                "MPN":MPN(femalle.id),
                #"TOPPN":TOPPN(femalle.id),
                #"BASPN":BASPN(femalle.id),
                #"MPS":MPS(femalle.id),
                #"TOPPS":TOPPS(femalle.id),
                #"BASPS":BASPS(femalle.id),
                
                
                "cons_moi":str(cons(femalle.id,age_revers(30),aujourdhui_date)/1000)+" kg",# la consomation pendant le dernier moi
                "cons_aujourdhui":str(cons(femalle.id,age_revers(0),aujourdhui_date)/1000)+" kg",# la consomation aujourd'hui
                "coup_cons_moi":str((cons(femalle.id,age_revers(30),aujourdhui_date)*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000)+" dt",
                "coup_cons_aujourdhui":str((cons(femalle.id,age_revers(0),aujourdhui_date)/1000*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000)+" dt",
              


                #'TPrp':TPrp(femalle.id,['california']),
                #'TPnetrp':TPnetrp(femalle.id,['california']),
                #'TMrp':TMrp(femalle.id,['california']),
                
                }              
                

                femalle={
                        'id':femalle.id,
                        "race":femalle.race,
                        "date_naissance":femalle.date_naissance,
                        "cage":femalle.cage,
                        "date_mort":femalle.date_mort,
                        "prix":femalle.prix,
                        "date_vent":femalle.date_vent,
                        "state":femalle.state,
                        'age':age_handler(age(str(femalle.date_naissance))),
                        'poid':poids,
                        'info':info,
                        }
                return Response(femalle,status=status.HTTP_200_OK)
            else:return Response(status=status.HTTP_404_NOT_FOUND)
        else:return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        if self.virif_femalle(id):
            if Femalle.objects.get(id=id).user==request.user:
                femalle=Femalle.objects.get(id=id)
                poids=PoidFemalle.objects.filter(femalle=femalle)
                for poid in poids:
                    poid.delete()
                femalle.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:return Response(status=status.HTTP_401_UNAUTHORIZED)    
        else:return Response(status=status.HTTP_404_NOT_FOUND)        
class MalleViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virif_malle(self,id):
        for malle in Malle.objects.all():
            if malle.id == id :
                return True
        return False    
    def put(self,request,id):
        if self.virif_malle(id) :
            if  Malle.objects.get(id=id).user==request.user:
                malle=Malle.objects.get(id=id)
                if age(str(malle.create_at))==0:
                    if malle.state=='production':
                        if age(request.data["date_naissance"])>=120:
                            malle.date_naissance=request.data.get('date_naissance')
                            malle.race=request.data.get("race")
                            malle.date_naissance=request.data.get("date_naissance")
                            malle.cage=request.data.get("cage")
                            malle.date_mort=request.data.get("date_mort")
                            malle.prix=request.data.get("prix")
                            malle.date_vent=request.data.get("date_vent")
                            malle.state=request.data.get('state')
                            malle.save()
                            poids=[]
                            for poid in PoidMalle.objects.filter(malle=malle):
                                poids.append(
                                            {
                                                'malle':str(poid.malle),
                                                'valeur':str(poid.valeur),
                                                'date_mesure':str(poid.date_mesure),
                                            })
                            malle={
                                    'id':malle.id,
                                    "race":malle.race,
                                    "date_naissance":malle.date_naissance,
                                    "cage":malle.cage,
                                    "date_mort":malle.date_mort,
                                    "prix":malle.prix,
                                    "date_vent":malle.date_vent,
                                    "state":malle.state,
                                    'age':age(str(malle.date_naissance)),
                                    'poid':poids,
                            }
                            return Response(malle,status=status.HTTP_202_ACCEPTED)
                        else:return Response("date not valid",status=status.HTTP_400_BAD_REQUEST)      # l'age d'un père doit etre super à 4 mois (120jours) 
                    else:return Response(status=status.HTTP_400_BAD_REQUEST)  
                else:return Response('tu peut pas changer les information d un malle apés '+str(age(str(malle.create_at)))+"jour de son ajout",status=status.HTTP_400_BAD_REQUEST)      
            else:return Response(status=status.HTTP_401_UNAUTHORIZED)        
        else:return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    def get(self,request,id):
        if self.virif_malle(id) :
            if Malle.objects.get(id=id).user==request.user:
                malle=Malle.objects.get(id=id)
                poids=[]
                for poid in PoidMalle.objects.filter(malle=malle):
                    poids.append(
                                {
                                    'femalle':str(poid.malle),
                                    'valeur':str(poid.valeur),
                                    'date_mesure':str(poid.date_mesure),
                                })
                return Response({'id':malle.id,"race":malle.race,"date_naissance":malle.date_naissance,"cage":malle.cage,"date_mort":malle.date_mort,"prix":malle.prix,"date_vent":malle.date_vent,"state":malle.state,'age':age(str(malle.date_naissance)),'poid':poids,},status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        if self.virif_malle(id):
            if Malle.objects.get(id=id).user==request.user:
                malle=Malle.objects.get(id=id)
                poids=PoidMalle.objects.filter(malle=malle)
                for poid in poids:
                    poid.delete()
                malle.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:return Response(status=status.HTTP_401_UNAUTHORIZED)    
        else:return Response(status=status.HTTP_404_NOT_FOUND) 

class CageVide(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"cage_vide":cage_vide(request.user)},status=status.HTTP_200_OK)
class FemalleProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virif_cage(self,cage):
        for malle in Femalle.objects.filter(user=self.request.user):
                    if cage == int((malle.cage)[1:]):
                        return True
        return False                
    def cage_vide (self):
        for i in range(1,len(Femalle.objects.filter(user=self.request.user))+1):
                if not self.virif_cage(i):
                    return 'F'+str(i)
        max=len(Femalle.objects.filter(user=self.request.user))
        return 'F'+str(max+1)
        # des fonctions du calcule pour calculer la prodectiviter d'une femalle
    def get(self,request):
        user=request.user
        lapins=[]
        lapins.clear() 
        for lapin in LapinProduction.objects.filter(user=user,state="production"):
            #if age(lapin.groupe.date_naissance)>=120:
                lapins.append({
                    'cage':lapin.cage,
                    'id':lapin.id,
                    "race":lapin.race,
                    "groupe":lapin.groupe.cage,
                }
                )   
        return Response(lapins,status=status.HTTP_200_OK)
    def post(self,request):
            lapin=LapinProduction.objects.get(id=request.data["lapin"])
            if lapin.user==request.user:
                if age(lapin.groupe.date_naissance)>=120:
                    user=request.user
                    femalle=Femalle.objects.create(race=request.data["race"],date_naissance=lapin.groupe.date_naissance,cage=self.cage_vide(),user=user)
                    femalle.save()
                    lapin.state="femalle"
                    lapin.save()
                    return Response(status=status.HTTP_201_CREATED)
                return Response("la femalle que vous voulez ajouter a un age trés petit",status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)














####################### clasic----views ###########################################################
# => *****FBV*****
@login_required    
def femalle_create(request):
    if request.method=='POST':
            form=FemalleForm(request.POST,request.FILES)
            if form.is_valid() :
                        instance=form.save(commit=False)
                        instance.user=request.user
                        
                        instance.save()
                        return redirect('femalle')
                            
    context={
            
            'form':FemalleForm,
            
        }      
    return render(request,'managment/parents/add_femalle.html',context)           

@login_required
def femalle_update(request,id):
    femalle= Femalle.objects.get(id=id)
    if request.method=='POST' and femalle.user==request.user:
        form=FemalleForm(request.POST,request.FILES,instance=femalle)
        if form.is_valid():
            form.save()
            return redirect('femalle')
    elif femalle.user==request.user :
        form=FemalleForm(instance=femalle)   
    if femalle.user==request.user:
            context ={
                'form':form,
            }
    else :
        return redirect('femalle')                 
    return render(request,"managment/parents/update_femalle.html",context)

@login_required
def femalle_morte(request,id):
    user=request.user
    femalle=Femalle.objects.get(id=id)
    if request.method=='POST' and femalle.user==request.user:
        form=FemalleMorte(request.POST,request.FILES,instance=femalle)
        if form.is_valid():
            form=form.save(commit=False)
            form.state='mort'
            form.save()
            return redirect('femalle') 
    info={}
    for lapin in Malle.objects.filter(user=user,state='production',id=femalle.id):
            info={
            'age':age(lapin.date_naissance),
            'id':lapin.id,
            }
    if femalle.user==request.user:
        context={
            'form':FemalleMorte,
            'id':id
       
        }
    else:
        return redirect('femalle')                 
    return render(request,'managment/parents/femalle_morte.html',context)
@login_required
def femalle_vendue(request,id):
    user=request.user
    msg=''
    femalle=Femalle.objects.get(id=id)
    if request.method=='POST' and femalle.user==request.user:
        form=FemalleVendue(request.POST,request.FILES,instance=femalle)
        if form.is_valid():
            form=form.save(commit=False)
            form.state='mort'
            form.save()
            return redirect('femalle')        
    info={}
    for lapin in Femalle.objects.filter(user=user,state='production',id=femalle.id):
            info={
            'age':age(lapin.date_naissance),
            'id':lapin.id,
            }        
    if femalle.user==request.user :
        context={
            "msg":msg,
            'form':FemalleVendue,
            'id':id,
            'info':info,
        }         
    else:
        return redirect('femalle')

    return render(request,'managment/parents/femalle_vendue.html',context)

@login_required
def malle_morte(request,id):
    user=request.user
    malle= Malle.objects.get(id=id)
    if request.method=='POST' and malle.user==request.user:
        malle_save=MalleMorte(request.POST,request.FILES,instance=malle)
        if malle_save.is_valid():
            form=malle_save.save(commit=False)
            form.state='mort'
            form.save()
            return redirect('malle') 
    info={}
    for lapin in Malle.objects.filter(user=user,state='production',id=malle.id):
            info={
            'age':age(lapin.date_naissance),
            'id':lapin.id,
            }        
    if malle.user==request.user:
        context={
            'form':MalleMorte,
            'id':id
       
        }
    else:
        return redirect('malle')                 
    return render(request,'managment/parents/malle_morte.html',context)
@login_required
def malle_vendue(request,id):
    user=request.user
    malle= Malle.objects.get(id=id)
    if request.method=='POST' and malle.user==request.user:
        malle_save=MalleVendue(request.POST,request.FILES,instance=malle)
        if malle_save.is_valid():
            form=malle_save.save(commit=False)
            form.state='mort'
            form.save()
            return redirect('malle') 
    info={}
    for lapin in Malle.objects.filter(user=user,state='production',id=malle.id):
            info={
            'age':age(lapin.date_naissance),
            'id':lapin.id,
            }       
    if malle.user==request.user :
        context={
            'form':MalleVendue,
            'id':id,
            'info':info
        }         
    else:
        return redirect('malle')

    return render(request,'managment/parents/malle_vendue.html',context)

@login_required
def femalle_details(request,id):
    femalle=Femalle.objects.get(id=id)
    user=request.user
    # des fonctions du calcule pour calculer la prodectiviter d'une femalle
    #TP : totale production d'une femalle dans ce mois retourner le nombre des lapin produite par cette femalle ce mois
    #TPnet :totale production d'une femalle dans ce mois à l'exclusion des lapins mortes retourner le nombre des lapin produite par cette femalle ce mois à l'exclusion des lapin mortes 
    #TP : totale des lapins mortes d'une femalle dans ce mois retourner le nombre des lapin mortes produite par cette femalle ce mois
    # en Formant f , m ou rp a la fin de ces noms pour dit que ces calcule sont fais pour une caterorie f : categorie des lapine m:categorie des malles et rp : categorie des lapin race pure 'californiaire'
    def TP(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():
                if idparent==groupe.acouplement.mère.id :
                    for lapin in LapinProduction.objects.all():
                        if lapin.groupe.id == groupe.id  :
                            nb=nb+1
            return nb                
    def TM(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():                    
                    if idparent==groupe.acouplement.mère.id :
                            for lapin in LapinProduction.objects.all():
                                        
                                        if lapin.groupe.id == groupe.id  and lapin.state=='mort':
                                            nb=nb+1
            return nb
    def TPnet(idparent):
            return TP(idparent)-TM(idparent)
    def TPm(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():
                if idparent==groupe.acouplement.mère.id:
                    for lapin in LapinProduction.objects.all():
                        if lapin.groupe.id == groupe.id  and lapin.sex=='malle':
                            nb=nb+1
            return nb
    def TMm(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():                    
                    if idparent==groupe.acouplement.mère.id :
                            for lapin in LapinProduction.objects.all():
                                        
                                        if lapin.groupe.id == groupe.id  and lapin.state=='mort' and lapin.sex=="malle":
                                            nb=nb+1
            return nb
    def TPnetm(idparent):
            return TPm(idparent)-TMm(idparent)
    def TPf(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():
                
                if idparent==groupe.acouplement.mère.id :
                    for lapin in LapinProduction.objects.all():
                        
                        if lapin.groupe.id == groupe.id  and lapin.sex=='femalle':
                            nb=nb+1
            return nb
    def TMf(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():                    
                    if idparent==groupe.acouplement.mère.id :
                            for lapin in LapinProduction.objects.all():
                                        
                                        if lapin.groupe.id == groupe.id  and lapin.state=='mort' and lapin.sex=="femalle":
                                            nb=nb+1
            return nb
    def TPnetf(idparent):
            return TPf(idparent)-TMf(idparent)
    def TPrp(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():
                
                if idparent==groupe.acouplement.mère.id :
                    for lapin in LapinProduction.objects.all():
                        
                        if lapin.groupe.id == groupe.id  and lapin.race=="californiaire":
                            nb=nb+1
            return nb
    def TMrp(idparent):
            nb=0
            for groupe in GroupeProduction.objects.all():                    
                    if idparent==groupe.acouplement.mère.id :
                            for lapin in LapinProduction.objects.all():
                                        
                                        if lapin.groupe.id == groupe.id  and lapin.state=='mort' and lapin.race=="californiaire":
                                            nb=nb+1
            return nb
    def TPnetrp(idparent):
            return TPrp(idparent)-TMrp(idparent)
   
    if user == femalle.user:
        info={
                'TPm':TPm(femalle.id),
                'TPnetm':TPnetm(femalle.id),
                'TMm':TMm(femalle.id),
                'TPf':TPf(femalle.id),
                'TPnetf':TPnetf(femalle.id),
                'TMf':TMf(femalle.id),
                'TPrp':TPrp(femalle.id),
                'TPnetrp':TPnetrp(femalle.id),
                'TMrp':TMrp(femalle.id),
                }
        context={
                     'femalle':femalle,
                     'infos':info,
            
                    }
    else:
        return redirect('malle')         
    return render(request,'managment/parents/details_femalle.html',context)

# => *****CBV*****
class MalleList(View):
    def render(self,request):
        user=request.user
        info=[]
        info.clear()
        for lapin in Malle.objects.filter(user=user,state='production'):
                info.append(
                {
                'age':age(lapin.date_naissance),
                #'ageMois':ageMois(lapin.date_naissance),
                #'ageSemaines':ageSemaines(lapin.date_naissance),
                #'ageAns':ageAns(lapin.date_naissance),
                'id':lapin.id,
                }
                )
        context={
                'malles':Malle.objects.filter(user=user,state='production'),
                'nombre_malles_morts':Malle.objects.filter(user=user,state='mort').count(),
                'nombre_malles_vendus':Malle.objects.filter(user=user,state='vendue').count(),
                'infos':info,
                
            }
        return render(request,'managment/parents/malle.html',context)
    def get(self,request):
        return self.render(request)     
class MalleCreate(View):
    def render(self,request):
        form=MalleForm
        return render(request,'managment/parents/add_malle.html',{'form':MalleForm})
    def get(self,request):
        return self.render(request)     
    def post(self,request):
        form=MalleForm(request.POST,request.FILES)
        if form.is_valid():
            new_user = Malle.objects.create(
                                            user=request.user, 
                                            date_naissance=request.POST['date_naissance'], 
                                            )
            return redirect('malle')
        return self.render(request)
class MalleUpdate(View):
    def render(self,request):
        form=MalleForm()
        return render(request,'managment/parents/update_malle.html',{'form':MalleForm})
    def get(self,request,id):
        return self.render(request)
    def post(self,request,id):
        malle= Malle.objects.get(id=id)
        if malle.user==request.user:
            form=MalleForm(request.POST,request.FILES,instance=malle)
            if form.is_valid():
                form.save()
                return redirect('malle')
        else :
            redirect('malle')          
class MalleDelete(View):
    def render(self,request):
        return render(request,'managment/parents/delete_malle.html')
    def get(self,request,id):
        malle= Malle.objects.get(id=id)
        if malle.user!=request.user :
            return redirect('malle')
        
        return self.render(request)
    def post(self,request,id):
        malle= Malle.objects.get(id=id)
        if malle.user==request.user:
            malle.delete()  
            return redirect('malle')
        else:
            return redirect('malle')  
        return self.render(request)      
class FemalleDelete(View):
    def render(self,request):
        return render(request,'managment/parents/delete_femalle.html')
    def get(self,request,id):
        femalle=Femalle.objects.get(id=id)
        if femalle.user!=request.user :
            return redirect('femalle')
        
        return self.render(request)
    def post(self,request,id):
        femalle= Femalle.objects.get(id=id)
        if femalle.user==request.user:
            femalle.delete()  
            return redirect('femalle')
        else:
            return redirect('femalle')  
        return self.render(request)            
class FemalleList(View):
    def render(self,request):
        user=request.user
        info=[]
        info.clear()
        for lapin in Femalle.objects.filter(user=user,state='production'):
                info.append(
                {
                'age':age(lapin.date_naissance),
                'ageMois':ageMois(lapin.date_naissance),
                'ageSemaines':ageSemaines(lapin.date_naissance),
                'ageAns':ageAns(lapin.date_naissance),
                'id':lapin.id,
                }
                )
        context={
                'femalles':Femalle.objects.filter(user=user,state='production'),
                'nombre_femalles_morts':Femalle.objects.filter(user=user,state='mort').count(),
                'nombre_femalles_vendus':Femalle.objects.filter(user=user,state='vendue').count(),
                'infos':info,
                
            }
        return render(request,'managment/parents/femalle.html',context)
    def get(self,request):
        return self.render(request)  