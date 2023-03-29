from email.policy import HTTP
from accounts.models import*
from django.shortcuts import redirect, render
from .models import*
from .forms import *
from .serializers import*
import os
from pathlib import Path
from PIL import Image
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from datetime import date
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .untils import *
aujourdhui_date=str(timezone.now().year)+"-"+str(timezone.now().month)+'-'+str(timezone.now().day)
base_path=str(Path(__file__).resolve().parent.parent)
base_path.replace(os.sep, '/')

############## API----WIEWS ##################### 
class FemalleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
        femalles=[]
        femalles.clear() 
        for femalle in Femalle.objects.filter(user=user):
                femalles.append({
                    'id':femalle.id,
                    "race":femalle.race.race,
                    #"cage":femalle.cage,
                    'img':str(femalle.img),
                    "state":femalle.state,
                    #'age':age_handler(age(str(femalle.date_naissance))),
                }
                )
                
        return Response(femalles,status=status.HTTP_200_OK)
    def post(self,request):
        if age(request.data["date_naissance"])>=120:
                user=request.user
                try :
                    femalle=Femalle.objects.create(img=request.data['file'],race=Race.objects.get(race=request.data["race"]),date_naissance=request.data["date_naissance"],cage=Femalle.cage_vide(user),user=user)
                except:
                     return Response('invalid data',status=status.HTTP_400_BAD_REQUEST)
                femalle.save()
                try :
                    basewidth = 200
                    img = Image.open(base_path+'/media/'+str(femalle.img))
                    wpercent = (basewidth/float(img.size[0]))
                    hsize = int((float(img.size[1])*float(wpercent)))
                    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
                    img.save(base_path+'/media/'+str(femalle.img))
                except:
                    femalle.delete_()
                    return Response('choisir une image',status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_201_CREATED)
        return Response("ladate de naissance invalide",status=status.HTTP_400_BAD_REQUEST)

class MalleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        malles=[]
        malles.clear()  
        for malle in Malle.objects.filter(user=user):
                malles.append(
                (
                {
                'id':malle.id,
                'img':str(malle.img),
                "race":malle.race.race,
                'age':age(str(malle.date_naissance)),
                'state':malle.state,
                })
                )
        return Response(malles,status=status.HTTP_200_OK)        
    def post(self,request):
            if age(request.data["date_naissance"])>=120:
                user=request.user
                try :
                    malle=Malle.objects.create(img=request.data['file'],race=Race.objects.get(race=request.data["race"]),date_naissance=request.data["date_naissance"],cage=Malle.cage_vide(user),user=user)
                except:
                     return Response('invalid data',status=status.HTTP_400_BAD_REQUEST)
                malle.save()
                try :
                    basewidth = 200
                    img = Image.open(base_path+'/media/'+str(malle.img))
                    wpercent = (basewidth/float(img.size[0]))
                    hsize = int((float(img.size[1])*float(wpercent)))
                    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
                    img.save(base_path+'/media/'+str(malle.img))
                except:
                    malle.delete_()
                    return Response('choisir une image',status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_201_CREATED)
            else:return Response("date de naissance invalide",status=status.HTTP_400_BAD_REQUEST)


class FemalleViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try :
            femalle=Femalle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  Femalle.objects.get(id=id).user==request.user:
            if age(str(femalle.create_at))==0:
                if femalle.state=='production':
                    if age(request.data["date_naissance"])>=120:
                        try :
                            femalle.date_naissance=request.data.get('date_naissance')  
                        except:
                             return Response('invalid date naissance',status=status.HTTP_400_BAD_REQUEST)
                        try :     
                            femalle.race.race=request.data.get("race")
                        except:
                             return Response('invalid race',status=status.HTTP_400_BAD_REQUEST)
                        try :
                            femalle.cage=request.data.get("cage")
                        except:
                             return Response('invalid cage',status=status.HTTP_400_BAD_REQUEST)
                        femalle.save()  
                        return Response(status=status.HTTP_202_ACCEPTED)     
                    else:return Response("date de naissance invalide",status=status.HTTP_400_BAD_REQUEST)  # l'age d'une mère doit etre super à 4 mois (120jours)    
                else:return Response(status=status.HTTP_400_BAD_REQUEST) 
            else:return Response('tu peut pas changer les information ',status=status.HTTP_400_BAD_REQUEST)           
        else:return Response(status=status.HTTP_401_UNAUTHORIZED)        
        
    def get(self,request,id):
        try :
            femalle=Femalle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Femalle.objects.get(id=id).user==request.user:
                femalle=Femalle.objects.get(id=id)
                # handling return : dernier groupe de production produit par cette femalle
                groupeprod=femalle.dernier_groupe_production()
                if (femalle.dernier_groupe_production()!=False):
                    groupeprod=femalle.dernier_groupe_production().id
                
                if femalle.dernier_groupe_production() == False or age(femalle.dernier_groupe_production().date_naissance) > 35:
                    info = {
                
                    'TP':0,
                    'TM':0,
                    'TMN':0,
                    'TPnet':0,
                    "dernière_groupe":groupeprod,
                    
    
                    #"MPDM":femalle.dernier_groupe_production().moyenne_poid_groupe_dernier_mesure(),
                    #"TOPPDM":femalle.dernier_groupe_production().TOPPDM(),
                    #"BASPDM":femalle.dernier_groupe_production().BASPDM(),
                    #"MPN":0,
                    #"TOPPN":femalle.dernier_groupe_production().TOPPN(),
                    #"BASPN":femalle.dernier_groupe_production().BASPN(),
                    #"MPS":0,
                    #"TOPPS":femalle.dernier_groupe_production().TOPPS(),
                    #"BASPS":femalle.dernier_groupe_production().BASP(),

                    "cons_moi":str(femalle.cons(age_revers(30),aujourdhui_date)/1000)+" kg",# la consomation pendant le dernier moi
                    "cons_aujourdhui":str(femalle.cons(age_revers(0),aujourdhui_date)/1000)+" kg",# la consomation aujourd'hui
                    "coup_cons_moi":str((femalle.cons(age_revers(30),aujourdhui_date)*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000)+" dt",
                    "coup_cons_aujourdhui":str((femalle.cons(age_revers(0),aujourdhui_date)/1000*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000)+" dt",
                
                    
                    }
                else :
                    info= {
                
                    'TP':femalle.dernier_groupe_production().nb_lapins_nées,
                    'TM':femalle.dernier_groupe_production().totale_mortalité_groupe(),
                    'TMN':femalle.dernier_groupe_production().nb_lapins_mortes_naissances,
                    'TPnet':femalle.dernier_groupe_production().nb_lapins_nées-femalle.dernier_groupe_production().totale_mortalité_groupe(),
                    "dernière_groupe":groupeprod,
                    
    
                    #"MPDM":femalle.dernier_groupe_production().moyenne_poid_groupe_dernier_mesure(),
                    #"TOPPDM":femalle.dernier_groupe_production().TOPPDM(),
                    #"BASPDM":femalle.dernier_groupe_production().BASPDM(),
                    #"MPN":femalle.dernier_groupe_production(),
                    #"TOPPN":femalle.dernier_groupe_production().TOPPN(),
                    #"BASPN":femalle.dernier_groupe_production().BASPN(),
                    #"MPS":femalle.dernier_groupe_production().moyenne_poid_groupe_souvrage(),
                    #"TOPPS":femalle.dernier_groupe_production().TOPPS(),
                    #"BASPS":femalle.dernier_groupe_production().BASP(),

                    "cons_moi":str(femalle.cons(age_revers(30),aujourdhui_date)/1000)+" kg",# la consomation pendant le dernier moi
                    "cons_aujourdhui":str(femalle.cons(age_revers(0),aujourdhui_date)/1000)+" kg",# la consomation aujourd'hui
                    "coup_cons_moi":str((femalle.cons(age_revers(30),aujourdhui_date)*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000)+" dt",
                    "coup_cons_aujourdhui":str((femalle.cons(age_revers(0),aujourdhui_date)/1000*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))/1000)+" dt",
                
                    
                    }   
                femalle={
                        'id':femalle.id,
                        "race":femalle.race.race,
                        "date_naissance":femalle.date_naissance,
                        "cage":femalle.cage,
                        "date_mort":femalle.date_mort,
                        "prix":femalle.prix,
                        "date_vent":femalle.date_vent,
                        "state":femalle.state,
                        'age':str(age(str(femalle.date_naissance)))+"j",
                        'poid':femalle.mesures_poids(),
                        'info':info,
                        }
                return Response(femalle,status=status.HTTP_200_OK)
            
        else:return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        try :
            femalle=Femalle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Femalle.objects.get(id=id).user==request.user:
                femalle.delete_()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:return Response(status=status.HTTP_404_NOT_FOUND)        

class MalleViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try :
            malle=Malle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  Malle.objects.get(id=id).user==request.user:
            if age(str(malle.create_at))==0:
                if malle.state=='production':
                    if age(request.data["date_naissance"])>=120:
                        try :
                            malle.date_naissance=request.data.get('date_naissance')  
                        except:
                             return Response('invalid date naissance',status=status.HTTP_400_BAD_REQUEST)
                        try :     
                            malle.race.race=request.data.get("race")
                        except:
                             return Response('invalid race',status=status.HTTP_400_BAD_REQUEST)
                        try :
                            malle.cage=request.data.get("cage")
                        except:
                             return Response('invalid cage',status=status.HTTP_400_BAD_REQUEST)
                        malle.save()  
                        return Response(status=status.HTTP_202_ACCEPTED)     
                    else:return Response("date de naissance invalide",status=status.HTTP_400_BAD_REQUEST)  # l'age d'une mère doit etre super à 4 mois (120jours)    
                else:return Response(status=status.HTTP_400_BAD_REQUEST) 
            else:return Response('tu peut pas changer les information ',status=status.HTTP_400_BAD_REQUEST)           
        else:return Response(status=status.HTTP_401_UNAUTHORIZED)        
        
    def get(self,request,id):
        try :
            malle=Malle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
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
                malle={
                       'id':malle.id,
                       "race":malle.race.race,
                       "date_naissance":malle.date_naissance,
                       "cage":malle.cage,
                       "date_mort":malle.date_mort,
                       "prix":malle.prix,
                       "date_vent":malle.date_vent,
                       "state":malle.state,
                       'age':age(str(malle.date_naissance)),
                       'poid':poids,
                       }
                return Response(malle,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        try :
            malle=Malle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Malle.objects.get(id=id).user==request.user:
                malle.delete_()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:return Response(status=status.HTTP_404_NOT_FOUND) 

class FemalleVentPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try :
            femalle=Femalle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  Femalle.objects.get(id=id).user==request.user:
                #if femalle.state=='production': 
                        prix=request.data.get("prix")
                        date_vent=request.data.get("date_vent")
                        return femalle.vent(prix,date_vent)      
                #else:return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:return Response(status=status.HTTP_404_NOT_FOUND)        
        
class MalleVentPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try :
            malle=Malle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  Malle.objects.get(id=id).user==request.user:
                if malle.state=='production': 
                        prix=request.data.get("prix")
                        date_vent=request.data.get("date_vent")
                        return malle.vent(prix,date_vent)      
                else:return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:return Response(status=status.HTTP_401_UNAUTHORIZED)               

class MalleMortPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try :
            malle=Malle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  Malle.objects.get(id=id).user==request.user:
                if malle.state=='production':
                        date_mort=request.data.get("date_mort")
                        return malle.mort(date_mort)
                else:return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:return Response(status=status.HTTP_401_UNAUTHORIZED) 

class FemalleMortPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try :
            femalle=Femalle.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if  Femalle.objects.get(id=id).user==request.user:
                if femalle.state=='production':
                        date_mort=request.data.get("date_mort")
                        return femalle.mort(date_mort)
                else:return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:return Response(status=status.HTTP_401_UNAUTHORIZED)        
       
     
# return un cage vide pour la criation d'une nouvelle femalle 
class CageVideFemalle(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"cage_vide":Femalle.cage_vide(request.user)},status=status.HTTP_200_OK)
class CageVideMalle(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"cage_vide":Malle.cage_vide(request.user)},status=status.HTTP_200_OK)

# fonction responsable a la creation d'une femalle a partir des lapin de production
class FemalleProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
                return Response("ladate de naissance invalide",status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
# fonction responsable a la creation d'un malle a partir des lapin de production
class MalleProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        lapins=[]
        lapins.clear() 
        for lapin in LapinProduction.objects.filter(user=user,state="production",sex='malle'):
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
                    malle=Malle.objects.create(race=request.data["race"],date_naissance=lapin.groupe.date_naissance,cage=self.cage_vide(),user=user)
                    malle.save()
                    lapin.delete()
                    return Response(status=status.HTTP_201_CREATED)
                return Response("ladate de naissance invalide",status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)

#######################""""production""################

############## API----WIEWS ##################### 
class AccouplementView(APIView):

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
        femalle=Femalle.objects.get(id=request.data["mère"])
        user=request.user
        malle=Malle.objects.get(id=request.data["père"])
        if  (femalle.est_acouplet() == False and femalle.user==user and femalle.state == "production") :# or femalle.id == acc.mère.id :
            if  (malle.user==user and malle.state == "production"):
                if age(request.data["date_acouplage"])>=0 and age(request.data["date_acouplage"])<=3:
                    acouplement=Accouplement(num=Accouplement.num_vide(request.user),user=request.user,père=Malle.objects.get(id=request.data["père"]),mère=Femalle.objects.get(id=request.data["mère"]),date_acouplage=request.data["date_acouplage"],test="non_vérifié",state='avant_naissance')
                    acouplement.save()
                    return Response(request.data["père"],status=status.HTTP_201_CREATED)
                else : return Response("invalid date",status=status.HTTP_400_BAD_REQUEST)
            else : return Response(" père not valid",status=status.HTTP_400_BAD_REQUEST)   
        else : return Response(" mère not valid",status=status.HTTP_400_BAD_REQUEST)

class AccouplementViewPk(APIView):
    def put(self,request,id):
        if Accouplement.objects.get(id=id).user==request.user:
                    acc=Accouplement.objects.get(id=id)
                    femalle=Femalle.objects.get(cage=request.data["mère"])
                    user=request.user
                    malle=request.data["père"]
                    if age(acc.create_at)<=1 :
                        if  (femalle.est_acouplet == False and femalle.user==user and femalle.state == "production")  or femalle.id == acc.mère.id :
                            if  (malle.user==user and malle.state == "production"):
                                if age(request.data["date_acouplage"])>=0 and age(request.data["date_acouplage"])<=3:
                                    acc.mère=Femalle.objects.get(cage=request.data["mère"])
                                    acc.père=Malle.objects.get(id=request.data["père"])
                                    acc.date_acouplage=request.data.get("date_acouplage")
                                    acc.create_at=timezone.now()
                                    acc.save() 
                                    return Response('information updated',status=status.HTTP_202_ACCEPTED)
                                else:return Response("date_acouplage not valid",status=status.HTTP_400_BAD_REQUEST)    
                            return Response("mère vendue ou morte",status=status.HTTP_400_BAD_REQUEST)
                        return Response("mère est déja acouplet ou vendue ou morte",status=status.HTTP_400_BAD_REQUEST)
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
    def get(self,request):
        user=request.user
        femalles=[]
        femalles.clear()   
        for femalle in Femalle.objects.filter(user=user,state="production"):
            
            if not femalle.est_acouplet(): 
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
                        "checked":False,# initialisation du var checked pour la js pour virifier les lapins choisies (mort,vent ...)
                        })
                
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
                    
                    "MoyPS":groupe.moyenne_poid_souvrage(),
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
            acouplement=Accouplement.objects.get(num=request.data["acouplement"])
            date_naissance=request.data["date_naissance"]
            nb_ln=request.data["nb_lapins_nées"]
            nb_lmn=request.data["nb_lapins_mortes_naissances"]
            if acouplement.user==user:
                if acouplement.test=="enceinte":
                    if bool(acouplement):# bool is a magic method for acc class that return True if the acc is befor acouplement period and False if the acc is after the acouplement period
                            if 2>age(date_naissance)>=0 and age(acouplement.date_acouplage)-age(date_naissance)>=27 and 20>=int(nb_ln)>=int(nb_lmn)>=0 and int(nb_ln)>0 :
                                if acouplement.mère.state =="production" :
                                    acouplement=acouplement
                                    acouplement.state="aprés_naissance"
                                    acouplement.save() 
                                    groupe=GroupeProduction.objects.create(acouplement=acouplement,date_naissance=date_naissance,cage=GroupeProduction.cage_vide(request.user),nb_lapins_nées=nb_ln ,nb_lapins_mortes_naissances=nb_lmn,user=user)
                                    groupe.save()
                                    return Response(status=status.HTTP_201_CREATED)
                            return Response("invalid data",status=status.HTTP_400_BAD_REQUEST)    
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
                accouplement=Accouplement.objects.get(num=request.data["acouplement"])
                date_naissance=request.data["date_naissance"]
                nb_ln=request.data["nb_lapins_nées"]
                nb_lmn=request.data["nb_lapins_mortes"]
                if 2>age(date_naissance)>=0 and age(accouplement.date_acouplage)-age(date_naissance)>=27 and 20>=int(nb_ln)>=int(nb_lmn)>=0 and int(nb_ln)>0 :
                        new_groupe=GroupeProduction.objects.create(cage=groupe.cage,acouplement=accouplement,date_naissance=date_naissance,nb_lapins_nées=nb_ln ,nb_lapins_mortes_naissances=nb_lmn,user=request.user)
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

######################"old views"#############################################
#"**************CBV **********
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
#########################################################

# *****FBV*******************
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