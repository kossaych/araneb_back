from accounts.models import*
from .models import*
from .forms import *
from .serializers import*
from .untils import *

from PIL import Image 
from django.utils import timezone
from email.policy import HTTP

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated


aujourdhui_date=str(timezone.now().year)+"-"+str(timezone.now().month)+'-'+str(timezone.now().day)


base_path=settings.BASE_DIR

############## API----WIEWS ##################### 

class FemalleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        user = request.user
        femalles = Femalle.objects.filter(user=user)

        serializer = Serializer(
                                 femalles,
                                 id='id',
                                 race='race', 
                                 img='img', 
                                 state='state', 
                                 age={'function': 'age', 'params': []},
                                 )
        
        serialized_data = serializer.serialize()
        if isinstance(serialized_data,dict):
                serialized_data = [serialized_data]
       
       
        return Response(serialized_data,status=status.HTTP_200_OK)
    
    
    def post(self,request,format=None):
        user=request.user 
        
        try :

            age_femalle_par_jour=age(request.data["date_naissance"])
        except :

            return Response('date naissance non valide',status=status.HTTP_400_BAD_REQUEST)
        if age_femalle_par_jour >= 120:
               
               
                try :
                    race_femalle=Race.objects.get(race=request.data["race"])
                except:
                     return Response('race non enregisté',status=status.HTTP_400_BAD_REQUEST)
               
               
               
                image_processor = ImageProcessor()
                if image_processor.verify_image(request.data['file']) :
                        femalle=Femalle.objects.create(img=request.data['file'],race=race_femalle,date_naissance=request.data["date_naissance"],cage=Femalle.cage_vide(user),user=user)
                        femalle.save()
                        # resize femalle's image
                        img_path = str(base_path)+'/media/'+str(femalle.img)
                        width =  300
                        height =  200
                        image_processor.resize_image(img_path,width,height)
                        return Response(status=status.HTTP_201_CREATED)
                
                return Response('invalid image',status=status.HTTP_400_BAD_REQUEST)

                    
                
        return Response("le date de naissance invalide",status=status.HTTP_400_BAD_REQUEST)

class MalleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user = request.user
        malles = Malle.objects.filter(user=user)

        serializer = Serializer(malles, id='id', race='race', img='img', state='state', age={'function': 'age', 'params': []})
        serialized_data = serializer.serialize()
        if isinstance(serialized_data,dict):
                serialized_data = [serialized_data]
        return Response(serialized_data,status=status.HTTP_200_OK)        
    def post(self,request,format=None):
        user=request.user 
        
        try :
            age_malle_par_jour=age(request.data["date_naissance"])
        except :
            return Response('date naissance non valide',status=status.HTTP_400_BAD_REQUEST)
        if age_malle_par_jour >= 120:
            try :
                    race_malle=Race.objects.get(race=request.data["race"])
            except:
                     return Response('race non enregisté',status=status.HTTP_400_BAD_REQUEST)
                
                
            image_processor = ImageProcessor()
            if image_processor.verify_image(request.data['file']) :
                        malle=Malle.objects.create(img=request.data['file'],race=race_malle,date_naissance=request.data["date_naissance"],cage=Malle.cage_vide(user),user=user)
                        malle.save()
                        # resize Malle's image
                        img_path = str(base_path)+'/media/'+str(malle.img)
                        width =  300 
                        height =  200
                        image_processor.resize_image(img_path,width,height)
                        return Response(status=status.HTTP_201_CREATED)
                
            return Response('invalid image',status=status.HTTP_400_BAD_REQUEST)

                    
                
        return Response("le date de naissance invalide",status=status.HTTP_400_BAD_REQUEST)
class FemalleViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id, format=None):
            try:
                female = Femalle.objects.get(id=id, user=request.user)
            except Femalle.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            try:
                age_female_per_day = age(request.data["date_of_birth"])
            except:
                return Response("Invalid date of birth", status=status.HTTP_400_BAD_REQUEST)
            
            if age(str(female.created_at)) == 0:
                if female.state == 'production':
                    if age_female_per_day >= 120:
                        try:
                            female.race.race = request.data.get("race")
                        except:
                            return Response('Race not registered', status=status.HTTP_400_BAD_REQUEST)
                        
                        female.save()
                        return Response(status=status.HTTP_202_ACCEPTED)
                    else:
                        return Response("A female cannot be younger than 4 months old",
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("You cannot change the information of this female",
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("You cannot change the information of a female after 24 hours of its creation",
                                status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id,format=None):
        try:
            # Fetch the Femalle object based on the provided id and user
            femalle = Femalle.objects.get(id=id, user=request.user)
        except Femalle.DoesNotExist:
            # Return a 404 Not Found response if the Femalle object does not exist
            return Response(status=status.HTTP_404_NOT_FOUND)

        statistiques = femalle.statistique()
        # Define the related field serializer for 'poid'
        poid_field = SerializerRelatedFieldRelationkeyInRelatedObject('femalle', PoidFemalle, {},
                                                                    date_mesure='date_mesure', valeur='valeur')
     
        # Serialize the 'femalle' object along with the related fields and statistics
        serializer = Serializer(femalle, id='id', race='race', state='state', date_naissance='date_naissance',
                                cage='cage', date_mort='date_mort', prix='prix', date_vent='date_vent',
                                poid=poid_field, age={'function': 'age', 'params': [],'fields':{}}, info=(statistiques,))
        serialized_data = serializer.serialize()

        return Response(serialized_data,status=status.HTTP_200_OK)
    
    def delete(self,request,id,format=None):
        try :
            femalle=Femalle.objects.get(id=id,user=request.user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        femalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MalleViewPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id, format=None):
            try:
                male = Malle.objects.get(id=id, user=request.user)
            except Malle.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            try:
                age_male_per_day = age(request.data["date_of_birth"])
            except:
                return Response("Invalid date of birth", status=status.HTTP_400_BAD_REQUEST)
            
            if age(str(male.created_at)) == 0:
                if male.state == 'production':
                    if age_male_per_day >= 120:
                        try:
                            male.race.race = request.data.get("race")
                        except:
                            return Response('Race not registered', status=status.HTTP_400_BAD_REQUEST)
                        
                        male.save()
                        return Response(status=status.HTTP_202_ACCEPTED)
                    else:
                        return Response("A male cannot be younger than 4 months old",
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("You cannot change the information of this male",
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("You cannot change the information of a male after 24 hours of its creation",
                                status=status.HTTP_400_BAD_REQUEST)
       
    def get(self,request,id,format=None):
        try:
            # Fetch the Malle object based on the provided id and user
            malle = Malle.objects.get(id=id, user=request.user)
        except Malle.DoesNotExist:
            # Return a 404 Not Found response if the Malle object does not exist
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Define the related field serializer for 'poid'
        poid_field = SerializerRelatedFieldRelationkeyInRelatedObject('malle', PoidMalle, {},
                                                                    date_mesure='date_mesure', valeur='valeur')

        # Create an instance of the Serializer class
        serializer = Serializer(malle,
                                id='id',
                                race='race',
                                state='state',
                                date_naissance='date_naissance',
                                cage='cage',
                                date_mort='date_mort',
                                prix='prix',
                                date_vent='date_vent',
                                poid=poid_field,
                                age={'function': 'age', 'params': []})

        # Serialize the object
        serialized_data = serializer.serialize()

        return Response(serialized_data,status=status.HTTP_200_OK)
    def delete(self,request,id,format=None):
        try :
            malle=Malle.objects.get(id=id,user=request.user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        malle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FemalleVentPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id,format=None):
        try :
            femalle=Femalle.objects.get(id=id,user=request.user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        prix=request.data.get("prix")
        date_vent=request.data.get("date_vent")
        return femalle.vent(prix,date_vent)      

class MalleVentPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id,format=None):
        try :
            malle=Malle.objects.get(id=id,user=request.user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        prix=request.data.get("prix")
        date_vent=request.data.get("date_vent")
        return malle.vent(prix,date_vent)      

class MalleMortPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id,format=None):
        try :
            malle=Malle.objects.get(id=id,user=request.user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        date_mort=request.data.get("date_mort")
        return malle.mort(date_mort)

class FemalleMortPk(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,id,format=None):
        try :
            femalle=Femalle.objects.get(id=id,user=request.user)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        date_mort=request.data.get("date_mort")
        return femalle.mort(date_mort)




# return un cage vide pour la criation d'une nouvelle femalle 
class CageVideFemalle(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        return Response({"cage_vide":Femalle.cage_vide(request.user)},status=status.HTTP_200_OK)
class CageVideMalle(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        return Response({"cage_vide":Malle.cage_vide(request.user)},status=status.HTTP_200_OK)

# fonction responsable a la creation d'une femalle a partir des lapin de production
class FemalleProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user=request.user
        lapins= LapinProduction.objects.filter(user=user,state="production")
        serializer = Serializer(lapins,cage='cage',id='id',race='race',groupe='groupe') 
        serialized_data = list(serializer.serialize())
        #serialized_data = [lapin for lapin in serialized_data if age(GroupeProduction.objects.get(cage=lapin['groupe']).date_naissance)>=120]
        return Response(serialized_data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
            lapin=LapinProduction.objects.get(id=request.data["lapin"])
            user=request.user
            if lapin.user == user:
                if age(lapin.groupe.date_naissance) >= 120 and lapin.sex == "femalle":

                    try :
                         race= Race.objects.get(race=request.data['race'])
                    except :
                         return Response('race non enregisté',status=status.HTTP_400_BAD_REQUEST)
                    
                    image_processor = ImageProcessor()
                    if image_processor.verify_image(request.data['image']) :
                        femalle=Femalle.objects.create(img = request.data['image'],race=race,date_naissance=lapin.groupe.date_naissance,cage=Femalle.cage_vide(user=user),user=user)
                        femalle.save()
                        # resize femalle's image
                        img_path = str(base_path)+'/media/'+str(femalle.img)
                        width =  300
                        height =  200
                        image_processor.resize_image(img_path,width,height)
                        lapin.delete_()
                        return Response(status=status.HTTP_201_CREATED)
                    return Response('invalid image', status = status.HTTP_400_BAD_REQUEST)
                return Response("la lapin choisie ne peut pas etre une femalle ",status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)

# fonction responsable a la creation d'un malle a partir des lapin de production
class MalleProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user=request.user
        lapins= LapinProduction.objects.filter(user=user,state="production")
        serializer = Serializer(lapins,cage='cage',id='id',race='race',groupe='groupe') 
        serialized_data = list(serializer.serialize())
        #serialized_data = [lapin for lapin in serialized_data if age(GroupeProduction.objects.get(cage=lapin['groupe']).date_naissance)>=120]
        return Response(serialized_data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
            lapin=LapinProduction.objects.get(id=request.data["lapin"])
            user=request.user
            if lapin.user == user:
                if age(lapin.groupe.date_naissance) >= 120 and lapin.sex=='malle':
                    try :
                         race= Race.objects.get(race=request.data['race'])
                    except :
                         return Response('race non enregisté',status=status.HTTP_400_BAD_REQUEST)
                    
                    image_processor = ImageProcessor()
                    if image_processor.verify_image(request.data['image']) :
                        malle=Malle.objects.create(img = request.data['image'],race=race,date_naissance=lapin.groupe.date_naissance,cage=Malle.cage_vide(user=user),user=user)
                        malle.save()
                        # resize malle's image
                        img_path = str(base_path)+'/media/'+str(malle.img)
                        width =  300
                        height =  200
                        image_processor.resize_image(img_path,width,height)
                        lapin.delete_()
                        return Response(status=status.HTTP_201_CREATED)
                    return Response('invalid image', status = status.HTTP_400_BAD_REQUEST)
                return Response("la lapin choisie ne peut pas etre une malle ",status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)

#######################""""production""################
############## API----WIEWS ##################### 
class AccouplementView(APIView):
    def get(self,request,format=None):
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
    def post(self,request,format=None):
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
    def put(self,request,id,format=None):
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
    def get(self,request,id,format=None):
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
    def delete(self,request,id,format=None):
        if Accouplement.objects.get(id=id):
            acc=Accouplement.objects.get(id=id)
            acc.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class AccouplementStateChangeView(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    def put(self,request,id,format=None):
        if Accouplement.objects.get(id=id).user==request.user:
            acc=Accouplement.objects.get(id=id)
            if age(acc.date_acouplage)<=35:
                    if age(acc.date_acouplage)>=27 and acc.test=='enciente':
                        acc.state=request.data.get("state")
                        acc.save() 
                        return Response('naissance enregistrer',status=status.HTTP_200_OK)
                    else:
                        return Response('test enregistrer',status=status.HTTP_200_OK)
            return Response("tu peut pas changer ces informations après 35 jour de date d'acouplage",status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)                

class AccouplementChangeTestView(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        def put(self,request,id,format=None):
            if Accouplement.objects.get(id=id):
                if Accouplement.objects.get(id=id).user==request.user:
                    acc=Accouplement.objects.get(id=id)
                    if age(acc.date_acouplage)<=35:
                            if age(acc.date_acouplage)>=9: 
                                if request.data.get("date_test") != "" and request.data.get("date_test") != "null" and (age(request.data.get("date_test"))>=32 or age(request.data.get("date_test"))>=0) and (request.data.get("test")=="enceinte" or request.data.get("test")=="pas enceinte"):
                                    acc.date_test=request.data.get("date_test")
                                    acc.test=request.data.get("test")
                                    acc.save()
                                    return Response(status=status.HTTP_200_OK)    
                                return Response("invalid data",status=status.HTTP_400_BAD_REQUEST)
                            return Response("tu peut pas faire un test de grossese avant 9 jour d'acouplage",status=status.HTTP_400_BAD_REQUEST)
                    else:return Response("tu peut pas changer ces informations après 35 jour de date d'acouplage",status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_404_NOT_FOUND)               
            return Response(status=status.HTTP_404_NOT_FOUND)               

class AccouplementFauseCoucheView(APIView):
        def put(self,request,id,format=None):
            if Accouplement.objects.get(id=id):
                if Accouplement.objects.get(id=id).user==request.user:
                    acc=Accouplement.objects.get(id=id)
                    if age(acc.date_acouplage)<=35:
                                if request.data.get("date_test") != "" and request.data.get("date_test") != "null" and age(request.data.get("date_test"))>=0 and age(acc.date_acouplage)-age(request.data.get("date_test"))>=0:
                                    acc.date_test=request.data.get("date_test")
                                    acc.test="fausse-couche"
                                    acc.save()
                                    return Response(status=status.HTTP_200_OK)    
                                return Response("date invalide",status=status.HTTP_400_BAD_REQUEST)
                    else:return Response("tu peut pas changer ces informations après 35 jour de date d'acouplage",status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_404_NOT_FOUND)               
            return Response(status=status.HTTP_404_NOT_FOUND)               

# retourner les femalle libre a acouplet
class FemallesAcouplementsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
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
    def get(self,request,format=None):
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
    def get(self,request,format=None):
        user=request.user
        groupes=[]
        groupes.clear() 
        for groupe in GroupeProduction.objects.filter(user=user):  
                lapins=[] 
                lapins.clear()  
                for lapin in LapinProduction.objects.filter(groupe=groupe,state="production"):
                    race = str(lapin.race)
                    lapins.append(
                        {
                        'id':lapin.id,
                        "sex":lapin.sex,
                        "race":race,
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
            
                totale_cons=groupe.cons_totale(groupe.date_naissance,aujourdhui_date)/1000
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
                



                    "cons":totale_cons,
                    "coup_cons":str((totale_cons*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))),
                    
                    
                    "TM":groupe.totale_mortalité_groupe(),                 
                    "MoyPS":groupe.moyenne_poid_souvrage(),
                    "MoyPN":groupe.moyenne_poid_groupe_naissance(),
                    "MoyPDM":groupe.moyenne_poid_groupe_dernier_mesure(),
                    "DateDMP":groupe.date_dernier_mesure(),
                    "Mpoids":groupe.moyenne_poid_groupe_list(),
                    "nbMalle":groupe.nombre_malle_groupe(),
                    "nbFemalle":groupe.nombre_femalle_groupe(),



                    "cons_auj":groupe.cons_totale(aujourdhui_date,aujourdhui_date)/1000,
                    "coup_cons_auj":str((groupe.cons_totale(age_revers(0),aujourdhui_date)/1000*(int(GeneralConfig.objects.get(user=request.user).coup_alimentation)))),
                    
                    "vaccins":vaccins,
                }
                )  
           
        return Response(groupes,status=status.HTTP_200_OK)
    def post(self,request,format=None):
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
    def put(self,request,id,format=None):
        if GroupeProduction.virif_groupe(id,request.user):
            groupe=GroupeProduction.objects.get(id=id)
            if 0>=age(groupe.create_at)<=1:
                accouplement=Accouplement.objects.get(num=request.data["acouplement"])
                date_naissance=request.data["date_naissance"]
                nb_ln=request.data["nb_lapins_nées"]
                nb_lmn=request.data["nb_lapins_mortes"]
                if 2>age(date_naissance)>=0 and age(accouplement.date_acouplage)-age(date_naissance)>=27 and 20>=int(nb_ln)>=int(nb_lmn)>=0 and int(nb_ln)>0 :
                        groupe.delete()
                        new_groupe=GroupeProduction.objects.create(cage=groupe.cage,acouplement=groupe.acouplement,date_naissance=date_naissance,nb_lapins_nées=nb_ln ,nb_lapins_mortes_naissances=nb_lmn,user=request.user)
                        new_groupe.save() 
                        return Response(status=status.HTTP_202_ACCEPTED)
                return Response("invalid data",status=status.HTTP_400_BAD_REQUEST)    
            return Response("tu peut pas changer ces information",status=status.HTTP_400_BAD_REQUEST)    
    
        return Response(status=status.HTTP_404_NOT_FOUND)              
    def get(self,request,id,format=None):
        if GroupeProduction.virif_groupe(id,request.user):
            lapins=[]
            lapins.clear()
            groupe=GroupeProduction.objects.get(id=id)
            for lapin in LapinProduction.objects.filter(groupe=groupe,state="production"):
                lapins.append(
                    {
                    "id":lapin.id,
                    "sex":lapin.sex,
                    "race":str(lapin.race),
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
    def delete(self,request,id,format=None):
        if GroupeProduction.virif_groupe(id,request.user):
            acc=GroupeProduction.objects.get(id=id).acouplement
            acc.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
     
class MortMasseLapinsProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
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
    def post(self,request,format=None):
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
    def post(self,request,id,format=None):
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
    def post(self,request,format=None):
        date=request.data['date_mesure']
        user=request.user
        valeurs=request.data['lapins']
        if age(LapinProduction.objects.get(id=valeurs[0]['id']).groupe.date_naissance)>= age(date) >=0 :
            for i in range(1,len(valeurs)):
                valeur=valeurs[i]['mesure']
                lapin=LapinProduction.objects.get(id=valeurs[i]['id'])
                if lapin.user == user and 0 <= int(valeurs[i]['mesure']) <= 5000 :
                    try :
                        old_poid=PoidLapinProduction.objects.get(lapin=lapin,date_mesure=date)
                        old_poid.date_mesure=date
                        old_poid.valeur=valeur
                        old_poid.save()
                    except:
                        poid=PoidLapinProduction(lapin=lapin,valeur=valeur,date_mesure=date)
                        poid.save()
                else:return  Response('la mesure du lapin'+str(LapinProduction.objects.get(id=valeurs[i]['id']).cage) +'doit etre compris entre 0 et 5000',status=status.HTTP_400_BAD_REQUEST)    
            return Response(status=status.HTTP_200_OK)    
                    
        return Response('invalid date de mesure',status=status.HTTP_400_BAD_REQUEST)    

class VaccinProductionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        if LapinProduction.objects.get(id=int(request.data['lapins'][0])).user==request.user :
            if age(LapinProduction.objects.get(id=int(request.data['lapins'][0])).groupe.date_naissance)>=age(request.data['date_vaccin'])>=0:
                for lapin in request.data['lapins']:
                    try :
                        vaccin=VaccinLapin(user=request.user,lapin=LapinProduction.objects.get(id=int(lapin)),date_vaccin=request.data['date_vaccin'],nom=request.data['nom_vaccin'],prix=request.data["prix_vaccin"],maladie=Maladie.objects.get(maladie=request.data["maladie_vaccin"]))
                    except:
                        return  Response("maladie n'est pas enregestrer ",status=status.HTTP_400_BAD_REQUEST)        
                    vaccin.save()
                return Response(status=status.HTTP_200_OK)   
            return Response('invalid date',status=status.HTTP_400_BAD_REQUEST)        
        return Response(status=status.HTTP_400_BAD_REQUEST)    

class LapinProductionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        lapins=LapinProduction.objects.filter(user=request.user)
        serializer=LapinProductionSerializer(lapins,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer=LapinProductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LapinProductionViewPk(APIView):
    def virif_lap(self,id,user):
        for lap in LapinProduction.objects.filter(user=user):
            if lap.id == id :
                return True
        return False    
        
    def put(self,request,id,format=None):
        if self.virif_lap(id,request.user):
            lap=LapinProduction.objects.get(id=id)
            try :
                lap.race=Race.objects.get(race=request.data['race'])
            except:
                return Response('invalid race',status=status.HTTP_400_BAD_REQUEST)
            try :
                lap.sex=request.data['sex']
            except:
                return Response('invalid sex',status=status.HTTP_400_BAD_REQUEST)
            lap.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id,format=None):
        if self.virif_lap(id,request.user):
                lap=LapinProduction.objects.get(id=id)
                data={
                    "id":str(lap.id),
                    "sex":lap.sex,
                    "race":lap.race,
                }
                return Response(data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id,format=None):
        if self.virif_lap(id,request.user):
            LapinProduction.objects.get(id=id).delete_()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


















# utilisé les viewsets au lieu des apiview
#from rest_framework.viewsets import ModelViewSet


'''
class VaccinFemalleView(ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = VaccinFemalle.objects.all()
    serializer_class =  VaccinFemalleSerializer
'''



























































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