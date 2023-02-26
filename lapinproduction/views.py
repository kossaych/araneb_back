from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import*
from .forms import *
from accounts.models import *
from parent.models import *
from .serializers import *
from datetime import date
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import date
aujourdhui_date=str(date.today())
# calculer l'age d'un lapin retourner le nombre de jour a partir du date de naissance (str!!) il retourne un entier
def age(naissance):
        """ naissance=str(naissance)
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
        str_d1 = str(naissance)
        aujourdhui_date=str(date.today())
        d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(aujourdhui_date, "%Y-%m-%d")
        age = str(d2 - d1)
        try :    
            age=int(age[:age.index('d')])
        except:
            age=0
        return  age
# retourner l'age en anné mois et jours sous forme str a partir du date de naissance
def age_handler(naissance):
        """      today=timezone.now()
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
                    #nb_mois=age


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
        """
        str_d1 = str(naissance)
        aujourdhui_date=str(date.today())
        d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(aujourdhui_date, "%Y-%m-%d")
        age=str(d2-d1)
        try :    
            age=(age[:age.index('d')])+" j"
        except:
            age="0 j"
        return str(age)                                
# retourner une liste contenant les dates succésivement a partir du intial_date jusqu'a final_date
def list_dates(initial_date,final_date):
    list_dates=[]
    (initial_date,final_date)
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

############## API----WIEWS ##################### 
class AccouplementView(APIView):
    
    def virif_mère(self,mère,user):
        test=True
        for acc in Accouplement.objects.filter(user=user,mère=mère):
            if age(acc.date_acouplage)<=35 and acc.state=="avant_naissance" and (acc.test=="enceinte" or acc.test=="non_vérifié"):
                test=False
        if Femalle.objects.get(id=int(mère)).state=="mort" or Femalle.objects.get(id=int(mère)).state=="vent":
            test=False
        return test 
    def virif_père(self,père,user):
        test=True
        if Malle.objects.get(id=int(père)).state=="mort" or Malle.objects.get(id=int(père)).state=="vent" or Malle.objects.get(id=int(père)).user!=user:
            test=False
        return test
    def get(self,request):
        accs=[]
        accs.clear()
        for acc in Accouplement.objects.filter(user=request.user):
            if age(acc.date_acouplage)<=35 and acc.state=="avant_naissance":
                accs.append({
                    'id':acc.id,
                    "num":acc.num,
                    "date_acouplage":acc.date_acouplage,
                    "père":acc.père.cage,
                    "mère":acc.mère.cage,
                    "test":acc.test,
                    "state":acc.state,
                    "date_test":acc.date_test,
                    'age':age(acc.date_acouplage),
                    "create_at":age(acc.create_at),

                })
        return Response(accs,status=status.HTTP_200_OK)
    def post(self,request):
        if self.virif_père(request.data["père"],request.user) and self.virif_mère(request.data["mère"],request.user):
            if age(request.data["date_acouplage"])>=0 and age(request.data["date_acouplage"])<=3:
                acouplement=Accouplement(num=Accouplement.num_vide(request.user),user=request.user,père=Malle.objects.get(id=request.data["père"]),mère=Femalle.objects.get(id=request.data["mère"]),date_acouplage=request.data["date_acouplage"],test="non_vérifié",state='avant_naissance')
                acouplement.save()
                return Response(request.data["père"],status=status.HTTP_201_CREATED)
            else : return Response("invalid date",status=status.HTTP_400_BAD_REQUEST)
        else : return Response("père or mère not valid",status=status.HTTP_400_BAD_REQUEST)

class AccouplementViewPk(APIView):
    
    def virif_mère(self,mère,user):
        test=True
        for acc in Accouplement.objects.filter(user=user,mère=mère):
            if  acc.state=="avant_naissance" and (acc.test=="enceinte" or acc.test=="non_vérifié"):
                test=False
        if Femalle.objects.get(id=int(mère)).state=="mort" or Femalle.objects.get(id=int(mère)).state=="vent":
            test=False
        return test 
    def virif_père(self,père,user):
        test=True
        if Malle.objects.get(id=père).state!="production" or Malle.objects.get(id=int(père)).user!=user:
            test=False
        return test 
    def put(self,request,id):
        if Accouplement.objects.get(id=id).user==request.user:
                    acc=Accouplement.objects.get(id=id)
                    if age(acc.create_at)<=1 :
                        if  (self.virif_père(request.data["père"],request.user) and self.virif_mère(Femalle.objects.get(cage=request.data["mère"]).id,request.user)) or Femalle.objects.get(cage=(request.data["mère"])).id == acc.mère.id:
                            if age(request.data["date_acouplage"])>=0 and age(request.data["date_acouplage"])<=3:
                                acc.mère=Femalle.objects.get(cage=request.data["mère"])
                                acc.père=Malle.objects.get(id=request.data["père"])
                                acc.date_acouplage=request.data.get("date_acouplage")
                                acc.create_at=timezone.now()
                                acc.save() 
                                return Response('information updated',status=status.HTTP_202_ACCEPTED)
                            else:return Response("date_acouplage not valid",status=status.HTTP_400_BAD_REQUEST)    
                        return Response("père or mère not valid",status=status.HTTP_400_BAD_REQUEST)
                    else:return Response("tu peut pas changer ces informations",status=status.HTTP_400_BAD_REQUEST)
            
        else:return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        if Accouplement.objects.get(id=id):
                acouplement={}
                acc=Accouplement.objects.get(id=id)
                acouplement={
                        "mère":acc.mère.cage,
                        "père":acc.père.id,
                        "date_acouplage":acc.date_acouplage,
                        "date_test":acc.date_test,
                        "test":acc.test,
                        "state":acc.state,
                        "create_at":(age_handler(acc.create_at)),
                    }
                return Response(acouplement,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        if Accouplement.objects.get(id=id):
            acc=Accouplement.objects.get(id=id)
            acc.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class AccouplementStateChangeView(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    def put(self,request,id):
        if Accouplement.objects.get(id=id).user==request.user:
            acc=Accouplement.objects.get(id=id)
            if age(acc.date_acouplage)<=32:
                    if age(acc.date_acouplage)>=27 and acc.test=='enciente':
                        acc.state=request.data.get("state")
                        acc.save() 
                        return Response('naissance enregistrer',status=status.HTTP_200_OK)
                    else:
                        return Response('test enregistrer',status=status.HTTP_200_OK)
            return Response("tu peut pas changer ces informations après 31 jour de date d'acouplage",status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)                

class AccouplementChangeTestView(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        def put(self,request,id):
            if Accouplement.objects.get(id=id):
                if Accouplement.objects.get(id=id).user==request.user:
                    acc=Accouplement.objects.get(id=id)
                    if age(acc.date_acouplage)<=32:
                            if age(acc.date_acouplage)>=9: 
                                if request.data.get("date_test") != "" and request.data.get("date_test") != "null" and (age(request.data.get("date_test"))>=32 or age(request.data.get("date_test"))>=0) and (request.data.get("test")=="enceinte" or request.data.get("test")=="pas enceinte"):
                                    acc.date_test=request.data.get("date_test")
                                    acc.test=request.data.get("test")
                                    acc.save()
                                    return Response(status=status.HTTP_200_OK)    
                                return Response("date invalide",status=status.HTTP_400_BAD_REQUEST)
                            return Response("tu peut pas faire un test de grossese avant 9 jour d'acouplage",status=status.HTTP_400_BAD_REQUEST)
                    else:return Response("tu peut pas changer ces informations après 32 jour de date d'acouplage",status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_404_NOT_FOUND)               
            return Response(status=status.HTTP_404_NOT_FOUND)               

class AccouplementFauseCoucheView(APIView):
        def put(self,request,id):
            if Accouplement.objects.get(id=id):
                if Accouplement.objects.get(id=id).user==request.user:
                    acc=Accouplement.objects.get(id=id)
                    if age(acc.date_acouplage)<=32:
                                if request.data.get("date_test") != "" and request.data.get("date_test") != "null" and age(request.data.get("date_test"))>=0 and age(acc.date_acouplage)-age(request.data.get("date_test"))>=0:
                                    acc.date_test=request.data.get("date_test")
                                    acc.test="fausse-couche"
                                    acc.save()
                                    return Response(status=status.HTTP_200_OK)    
                                return Response("date invalide",status=status.HTTP_400_BAD_REQUEST)
                    else:return Response("tu peut pas changer ces informations après 32 jour de date d'acouplage",status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_404_NOT_FOUND)               
            return Response(status=status.HTTP_404_NOT_FOUND)               

# retourner les femalle libre a acouplet
class FemallesAcouplementsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virif_acouplement(self,femalle,user):
        for acc in Accouplement.objects.filter(user=user,mère=femalle,state="avant_naissance"):
            if (acc.test=="enceinte" or acc.test=="non_vérifié"):
                return False
        return True
    def get(self,request):
        user=request.user
        femalles=[]
        femalles.clear() 
     
        for femalle in Femalle.objects.filter(user=user,state="production"):
            if self.virif_acouplement(femalle.id,user.id): 
                femalles.append({
                    'id':femalle.id,
                    "cage":femalle.cage,  
                }
                )
        
        return Response(femalles,status=status.HTTP_200_OK)
# retourner les malles libres a acouplet
class MallesAcouplementsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
      
        malles=[]
        malles.clear() 
        for malle in Malle.objects.filter(user=user,state="production"):
                malles.append({
                    'id':malle.id,
                    "cage":malle.cage,  
                }
                )    
        return Response(malles,status=status.HTTP_200_OK)

class ProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def virf_acc(self,acc,user):
        test=True
        for groupe in GroupeProduction.objects.filter(user=user):
            if groupe.acouplement.num==acc:
                test=False
        return test
    def get(self,request):
        user=request.user
        groupes=[]
        groupes.clear() 
        for groupe in GroupeProduction.objects.filter(user=user):
                lapins=[]
                lapins.clear()
                for lapin in LapinProduction.objects.filter(groupe=groupe,state="production"):
                    lapins.append(
                        {
                        'id':lapin.id,
                        "sex":lapin.sex,
                        "race":lapin.race,
                        "cage":lapin.cage,
                        "PN":lapin.poid_naissance(),#poid a la naissance 
                        "PDM":lapin.poid_dernier_mesure(),#poid la dernière mesure
                        "PS":lapin.poid_sevrage(),
                        "Poids":lapin.poid_lapin_list(),
                        "vaccin":lapin.vaccins(),
                        "checked":False,# initialisation du var chec pour la js pour virifier les lapins choisies
                        })
                MoyPS="y'a pas des mesure"
                if groupe.date_souvrage!=None:   
                    for poid in groupe.moyenne_poid_groupe_list():
                        if poid['date']==age(groupe.date_naissance)-age(groupe.date_souvrage):
                            MoyPS=int(poid['mesure'])
                vaccins=[]
                for vaccin in VaccinLapin.objects.filter(user=request.user):
                    if vaccin.lapin.groupe==groupe:   
                        existe=False
                        for vacc in vaccins:
                            if vaccin.nom == (vacc['nom']) and age_handler(vaccin.date_vaccin)== (vacc['date_vaccin']) :#and vaccin.maladie == (vacc['maladie']):
                                existe=True
                                vacc=vacc
                                break
                                
                        if not existe :    
                            vaccins.append(
                                {
                                    'lapins':[vaccin.lapin.id,],
                                    "nom":str(vaccin.nom),
                                    "date_vaccin":str(age_handler(vaccin.date_vaccin)),
                                    "prix":str(vaccin.prix),
                                    "maladie":str(vaccin.maladie),
                                }
                            )    
                        else : 
                            vacc['prix']=int(vacc['prix'])+int(vaccin.prix)  
                            vacc['lapins'].append(vaccin.lapin.id)
                    
                groupes.append({
                    "acc_num":groupe.acouplement.num,
                    'id':groupe.id,
                    "date_naissance":groupe.date_naissance,
                    "cage":groupe.cage,
                    'age':(age_handler(groupe.date_naissance)),
                    'lapins':lapins,#liste des lapins de groupe
                    "date_souvrage":groupe.date_souvrage,
                    "nb_lapins_nées":groupe.nb_lapins_nées,
                    "nb_lapins_mortes_naissances":groupe.nb_lapins_mortes_naissances,
                    "père":groupe.acouplement.père.cage,
                    "mère":groupe.acouplement.mère.cage,
                    "date_acouplage":groupe.acouplement.date_acouplage,
                    "TM":groupe.totale_mortalité_groupe(),
                    
                    "MoyPS":MoyPS,
                    "MoyPN":groupe.moyenne_poid_groupe_naissance(),
                    "MoyPDM":groupe.moyenne_poid_groupe_dernier_mesure(),
                    "DateDMP":groupe.date_dernier_mesure(),
                    "Mpoids":groupe.moyenne_poid_groupe_list(),
                    "nbMalle":groupe.nombre_malle_groupe(),
                    "nbFemalle":groupe.nombre_femalle_groupe(),

                    "cons":groupe.cons_totale(groupe.date_naissance,aujourdhui_date)/1000,
                    "cons_auj":groupe.cons_totale(aujourdhui_date,aujourdhui_date)/1000,
                   
                    "coup_cons":str((groupe.cons_totale(age_revers(30),aujourdhui_date)/1000*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000),
                    "coup_cons_auj":str((groupe.cons_totale(age_revers(0),aujourdhui_date)/1000*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000),
              
                    "vaccins":vaccins,


                }
                )
                
        return Response(groupes,status=status.HTTP_200_OK)
    def post(self,request):
            user=request.user
            if Accouplement.objects.get(num=request.data["acouplement"]).user==user:
                if  Accouplement.objects.get(num=request.data["acouplement"]).test=="enceinte":
                    if  self.virf_acc(request.data["acouplement"],user) == True:
                        if age(Accouplement.objects.get(num=request.data["acouplement"]).date_acouplage)>27:
                            if age(Accouplement.objects.get(num=request.data["acouplement"]).date_acouplage)-27>=age(request.data["date_naissance"]) and 20>=int(request.data["nb_lapins_nées"])>=int(request.data["nb_lapins_mortes_naissances"])>=0 :
                                if Accouplement.objects.get(num=request.data["acouplement"]).mère.state =="production" :
                                    acouplement=Accouplement.objects.get(num=request.data["acouplement"])
                                    acouplement.state="aprés_naissance"
                                    acouplement.save() 
                                    groupe=GroupeProduction.objects.create(acouplement=Accouplement.objects.get(num=request.data["acouplement"]),date_naissance=request.data["date_naissance"],cage=GroupeProduction.cage_vide(request.user),nb_lapins_nées=request.data["nb_lapins_nées"] ,nb_lapins_mortes_naissances=request.data["nb_lapins_mortes_naissances"],user=user)
                                    groupe.save()
                                    return Response(status=status.HTTP_201_CREATED)
                            return Response("invalid data",status=status.HTTP_400_BAD_REQUEST)    
                        return Response("acouplement ne finie pas la periode de grossesse",status=status.HTTP_400_BAD_REQUEST)
                    return Response("تم استعمال هذا التزاوج سابقا",status=status.HTTP_400_BAD_REQUEST)
                return Response("لم يتم التحقق بعد ما اذا كانت حامل",status=status.HTTP_400_BAD_REQUEST)
            return Response("acouplement not found",status=status.HTTP_404_NOT_FOUND)
    
class ProductionViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]      
    def put(self,request,id):
        if GroupeProduction.virif_groupe(id,request.user):
            groupe=GroupeProduction.objects.get(id=id)
            if 0>=age(groupe.create_at)<=1:
                if age(Accouplement.objects.get(num=request.data["acouplement"]).date_acouplage)-27>=age(request.data["date_naissance"]) and 20>=int(request.data["nb_lapins_nées"])>=int(request.data["nb_lapins_mortes"])>=0 and int(request.data["nb_lapins_nées"])>0 and 2>age(request.data["date_naissance"])>=0:
                        new_groupe=GroupeProduction.objects.create(cage=groupe.cage,acouplement=Accouplement.objects.get(num=request.data["acouplement"]),date_naissance=request.data["date_naissance"],nb_lapins_nées=request.data["nb_lapins_nées"] ,nb_lapins_mortes_naissances=request.data["nb_lapins_mortes"],user=request.user)
                        groupe.delete()
                        new_groupe.save() 
                        return Response(status=status.HTTP_202_ACCEPTED)
                return Response("invalid data",status=status.HTTP_400_BAD_REQUEST)    
            return Response("tu peut pas changer ces information",status=status.HTTP_400_BAD_REQUEST)    
    
        return Response(status=status.HTTP_404_NOT_FOUND)              
    def get(self,request,id):
        if GroupeProduction.virif_groupe(id,request.user):
            lapins=[]
            lapins.clear()
            groupe=GroupeProduction.objects.get(id=id)
            for lapin in LapinProduction.objects.filter(groupe=groupe,state="production"):
                lapins.append(
                    {
                    "id":lapin.id,
                    "sex":lapin.sex,
                    "race":lapin.race,
                    "cage":lapin.cage,
                    "date_mort":lapin.date_mort,
                    "prix":lapin.prix,
                    "date_vent":lapin.date_vent,
                    })
            groupe={
                "acc_num":groupe.acouplement.num,
                'id':groupe.id,
                "date_naissance":groupe.date_naissance,
                "cage":groupe.cage,
                'age':(age_handler(groupe.date_naissance)),
                'lapins':lapins,#liste des lapins de groupe
                "date_souvrage":groupe.date_souvrage,
                "nb_lapins_nées":groupe.nb_lapins_nées,
                "nb_lapins_mortes_naissances":groupe.nb_lapins_mortes_naissances,
                "père":groupe.acouplement.père.cage,
                "mère":groupe.acouplement.mère.cage,
                "date_acouplage":groupe.acouplement.date_acouplage,
                "TM":groupe.totale_mortalité_groupe(),
                "MoyPN":groupe.moyenne_poid_groupe_naissance(),
                "MoyPDM":groupe.moyenne_poid_groupe_dernier_mesure(),
                "DateDMP":groupe.date_dernier_mesure(),
                "Mpoids":groupe.moyenne_poid_groupe_list(),
                "nbMalle":groupe.nombre_malle_groupe(),
                "nbFemalle":groupe.nombre_femalle_groupe(),
            }
            return Response(groupe,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        if GroupeProduction.virif_groupe(id,request.user):
            acc=GroupeProduction.objects.get(id=id).acouplement
            acc.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
     
class MortMasseLapinsProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        if age(LapinProduction.objects.get(id=request.data['lapins'][0]).groupe.date_naissance)>=age(request.data['date_mort'])>=0:
            for lapin in request.data['lapins']:
                lapin=LapinProduction.objects.get(id=lapin)
                lapin.state="mort"
                lapin.date_mort=request.data['date_mort']
                lapin.save()
            return Response(status=status.HTTP_200_OK)    
        return Response(status=status.HTTP_400_BAD_REQUEST)    

class VenteMasseLapinsProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        lapins=[]
        for lap in request.data['lapins']:
            if lap=={}:
                pass
            else :
                lapins.append(lap)

        if age(LapinProduction.objects.get(id=lapins[0]['id']).groupe.date_naissance)>=age(request.data['date_vente'])>=0:
            for lap in lapins:
                
                    lapin=LapinProduction.objects.get(id=lap['id'])
                    lapin.state="vendue"
                    lapin.prix=lap['price']
                    lapin.save()
                
            return Response(status=status.HTTP_200_OK)    
        return Response(status=status.HTTP_400_BAD_REQUEST)    
                        
class SevrageProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,id):
        if GroupeProduction.objects.get(id=int(request.data['groupe'])).user==request.user :
            if age(GroupeProduction.objects.get(id=int(request.data['groupe'])).date_naissance)-25>=age(request.data['date_sevrage'])>=0:
                groupe=GroupeProduction.objects.get(id=int(request.data['groupe']))
                groupe.date_souvrage=request.data['date_sevrage']
                groupe.save()
                return Response(status=status.HTTP_200_OK)   
            return Response('tu peut pas sevrer ce groupe avant passer 25 jours de son naissance',status=status.HTTP_400_BAD_REQUEST)        
        return Response(status=status.HTTP_400_BAD_REQUEST)    
                        
class PoidLapinProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        date=request.data['date_mesure']
        user=request.user
        valeurs=request.data['lapins']
        if age(LapinProduction.objects.get(id=valeurs[0]['id']).groupe.date_naissance)>= age(date) >=0 :
            for i in range(1,len(valeurs)):
                valeur=valeurs[i]['mesure']
                lapin=LapinProduction.objects.get(id=valeurs[i]['id'])
                if lapin.user == user and 0 <= int(valeurs[i]['mesure']) <= 5000 : 
                    poid=PoidLapinProduction(lapin=lapin,valeur=valeur,date_mesure=date)
                    poid.save()
                else:return  Response('la mesure du lapin'+str(LapinProduction.objects.get(id=valeurs[i]['id']).cage) +'doit etre compris entre 0 et 5000',status=status.HTTP_400_BAD_REQUEST)    
            return Response(status=status.HTTP_200_OK)    
                    
        return Response('invalid date de mesure',status=status.HTTP_400_BAD_REQUEST)    

class VaccinProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        if LapinProduction.objects.get(id=int(request.data['lapins'][0])).user==request.user :
            if age(LapinProduction.objects.get(id=int(request.data['lapins'][0])).groupe.date_naissance)>=age(request.data['date_vaccin'])>=0:
                for lapin in request.data['lapins']:
                    vaccin=VaccinLapin(user=request.user,lapin=LapinProduction.objects.get(id=int(lapin)),date_vaccin=request.data['date_vaccin'],nom=request.data['nom_vaccin'],prix=request.data["prix_vaccin"],maladie=request.data["maladie_vaccin"])
                    vaccin.save()
                return Response(status=status.HTTP_200_OK)   
            return Response('invalid date',status=status.HTTP_400_BAD_REQUEST)        
        return Response(status=status.HTTP_400_BAD_REQUEST)    
    
class LapinProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        lapins=LapinProduction.objects.filter(user=request.user)
        serializer=LapinProductionSerializer(lapins,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=LapinProductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serialier.data,status=status.HTTP_400_BAD_REQUEST)
class LapinProductionViewPk(APIView):
    def virif_lap(self,id,user):
        for lap in LapinProduction.objects.filter(user=user):
            if lap.id == id :
                return True
        return False    
        
    def put(self,request,id):
        if self.virif_lap(id,request.user):
            lap=LapinProduction.objects.get(id=id)
            lap.race=request.data['race']
            lap.sex=request.data['sex']
            lap.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        if self.virif_lap(id,request.user):
                lap=LapinProduction.objects.get(id=id)
                data={
                    "id":str(lap.id),
                    "sex":lap.sex,
                    "race":lap.race,
                }
                return Response(data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        if self.virif_lap(id,request.user):
            lap=LapinProduction.objects.get(id=id)
            lap.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
     
############ CBV ###########
class ProductionList(ListView):
    model:GroupeProduction
    template_name = 'managment/production/production.html'
    def get_queryset(self):
        return GroupeProduction.objects.filter(user=self.request.user)
    
  
    def get_context_data(self, **kwargs):
        info=[]
        info.clear()
        for groupe in GroupeProduction.objects.filter(user=self.request.user):
                    info.append(
                    {
                    'age':age(groupe.date_naissance),
                    'ageMois':ageMois(groupe.date_naissance),
                    'ageSemaines':ageSemaines(groupe.date_naissance),
                    'ageAns':ageAns(groupe.date_naissance),
                    'id':groupe.id,
                    }
                    )
        context = super().get_context_data(**kwargs)
        context['lapins'] =LapinProduction.objects.filter(user=self.request.user,state='production')
        accouplements=[]
        for acc in Accouplement.objects.filter(user=self.request.user,state='avant_naissance'):
            if acc.test in ['non_vérifié','enceinte'] :
                accouplements.append(acc)
        context['accouplements'] =accouplements
        context['infos'] =info
        return context
class GroupeProductionCreate(LoginRequiredMixin,View):
    def virif_cage(self,cage):
        for groupe in GroupeProduction.objects.filter(user=self.request.user):
                    if cage == int((groupe.cage)[1:]):
                        return True
        return False                
    def cage_vide (self):
        for i in range(1,len(GroupeProduction.objects.filter(user=self.request.user))+1):
                if not self.virif_cage(i):
                    return 'G'+str(i)
        max=0
        for groupe in GroupeProduction.objects.filter(user=self.request.user):
            if int(groupe.cage[1:])>max:
                max=int(groupe.cage[1:])
        return 'G'+str(max+1)        


        return  'G'+str(i)
    def render(self,request):
        form=GroupeProductionForm
        acouplements=Accouplement.objects.filter(user=self.request.user)
        return render(request,'managment/production/add_groupe_production.html',{'form':GroupeProductionForm,'cage':self.cage_vide(),"acouplements":acouplements,})
    def get(self,request):
        return self.render(request)                    
    def post(self,request):
        form=GroupeProductionForm(request.POST,request.FILES)
        if form.is_valid():
            GroupeProduction.objects.create(
                                            cage=self.cage_vide(),
                                            user=request.user,
                                            date_naissance=request.POST['date_naissance'],
                                            #acouplement=request.POST['acouplement'],
                                            nb_lapins_nées=request.POST['nb_lapins_nées'],
                                            nb_lapins_mortes_naissances=request.POST['nb_lapins_mortes_naissances'],
                                            )
            return redirect('production')
        return self.render(request)
class AcouplementCreate(LoginRequiredMixin,View):
    def virif_num(self,num):
        for groupe in Accouplement.objects.filter(user=self.request.user):
                    if num == int((groupe.num)[1:]):
                        return True
        return False                
    def num_vide (self):
        for i in range(1,len(Accouplement.objects.filter(user=self.request.user))+1):
                if not self.virif_num(i):
                    return 'A'+str(i)
        max=0
        for groupe in Accouplement.objects.filter(user=self.request.user):
            if int(groupe.num[1:])>max:
                max=int(groupe.num[1:])
        return 'A'+str(max+1)        


        return  'A'+str(i)
    def render(self,request):
        form=AccouplementForm
        malles=Malle.objects.filter(user=request.user,state='production')
        femalles=Femalle.objects.filter(user=request.user,state='production')
        
        return render(request,'managment/production/add_accouplement.html',{'form':AccouplementForm,'num':self.num_vide(),'malles':malles,'femalles':femalles})
    def get(self,request):
        return self.render(request)     
               
    def post(self,request):
        form=AccouplementForm(request.POST,request.FILES)
        if form.is_valid():
            Accouplement.objects.create(
                                            num=self.num_vide(),
                                            user=request.user,
                                            date_acouplage=request.POST['date_acouplage'],
                                            père=Malle.objects.get(id=request.POST['père']),
                                            mère=Femalle.objects.get(id=request.POST['mère']),
                                        )
            return redirect('production')
        return self.render(request)
