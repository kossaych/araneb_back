from django.db import models
from parent.models import Malle
from parent.models import Femalle
from accounts.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime,date
#import pandas as pd 
from accounts.models import Race
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
        age = jours_anné+jours_moi+ (today.day - jour) """
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
    
    

    for year in range(int(initial_date[:initial_date.index('-')]),int(final_date[:final_date.index('-')])+1):
            print(year)
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
                                    date=str(year)+"-"+(moi_date)+"-"+(jour_date)    
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
                                    date=str(year)+"-"+(moi_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
                                    
                if moi == 2 :
                    if (year%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if year %400==0:
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
                                    date=str(year)+"-"+(moi_date)+"-"+(jour_date)    
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
                                    date=str(year)+"-"+(moi_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
                                    
                    else:
                            if year %4==0:
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
                                    date=str(year)+"-"+(moi_date)+"-"+(jour_date)    
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
                                    date=str(year)+"-"+(moi_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
    return list_dates[list_dates.index(initial_date):list_dates.index(final_date)+1]        
 
class Accouplement(models.Model):
    TEST_ACOUPLAGE =[
            ('pas_enceinte','pas enceinte'),
            ('enceinte','enceinte'),
            ('non_vérifié','non vérifié'),
            ('fausse_couche','fausse-couche')
    ]
    STATE_ACOUPLAGE =[
            ('avant_naissance','avant_naissance'),
            ('aprés_naissance','aprés_naissance'),
    ]
    create_at=models.DateField(default=timezone.now)
    num=models.CharField(max_length=50,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True)
    père=models.ForeignKey(Malle,on_delete=models.CASCADE,null=True , blank=True)
    mère=models.ForeignKey(Femalle,on_delete=models.CASCADE,null=True , blank=True)
    date_acouplage=models.DateField(default=timezone.now)
    date_fausse_couche=models.DateField(null=True , blank=True)
    date_test=models.DateField(null=True , blank=True)
    test=models.CharField(choices=TEST_ACOUPLAGE ,max_length=200,default='non_vérifié')
    state=models.CharField(choices=STATE_ACOUPLAGE ,max_length=200,default='avant_naissance')
    @classmethod
    def virif_num(cli,num,user):
        for acc in cli.objects.filter(user=user):
                    if num == int((acc.num)[1:]):
                        return True
        return False                
    @classmethod    
    def num_vide (cli,user):
        for i in range(1,len(cli.objects.filter(user=user))+1):
                if not cli.virif_num(i,user):
                    return 'A'+str(i)
        max=0
        for acc in cli.objects.filter(user=user):
            if int(acc.num[1:])>max:
                max=int(acc.num[1:])
        return 'A'+str(max+1)        
    def __str__(self):
        return str(self.num)
class GroupeProduction(models.Model):
        #information principale
        create_at=models.DateField(default=timezone.now)
        cage=models.CharField(max_length=50,null=True,blank=True)
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True)
        acouplement=models.ForeignKey(Accouplement,on_delete=models.CASCADE,null=True , blank=True)
        date_naissance=models.DateField(null=True , blank=True)
        date_souvrage=models.DateField(null=True , blank=True)
        #information de naissance
        nb_lapins_nées=models.IntegerField(default=0)
        nb_lapins_mortes_naissances=models.IntegerField(default=0)
        @classmethod
        # verifier si un cage vide ou non
        def virif_cage(cls,cage,user):
            for groupe in cls.objects.filter(user=user):
                        if cage == int((groupe.cage)[1:]):
                            return True
            return False  
        @classmethod
        # retoiurner un cage vide pour les naveaux groupe    
        def cage_vide (cls,user):
            for i in range(1,len(cls.objects.filter(user=user))+1):
                    if not cls.virif_cage(i,user):
                        return 'G'+str(i)
            max=0
            for groupe in cls.objects.filter(user=user):
                if int(groupe.cage[1:])>max:
                    max=int(groupe.cage[1:])
            return 'G'+str(max+1)        
        @classmethod    
        # verifier l'existance d'un groupe 
        def virif_groupe(cls,id,user):
            for groupe in cls.objects.filter(user=user):
                if groupe.id == id :
                    return True
            return False 
        # totale des lapins morte dans le groupe
        def totale_mortalité_groupe(self):
            nb=0
            for lapin in LapinProduction.objects.filter(groupe=self.id):
                if lapin.state=="mort":
                        nb=nb+1
            return nb
        # moyenne des poids des lapins des productions d'un groupe a la naissance
        def moyenne_poid_groupe_naissance(self):
            moy=0
            nb=0
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.groupe.id==self.id:
                        if poid.date_mesure==poid.lapin.groupe.date_naissance:
                            nb=nb+1
                            moy=moy+poid.valeur
            if nb!=0:
                return int(moy/nb)
            else:
                return "y'a pas des mesures"    
        # retourner la dernier date de mesure des poids du groupe de production
        def date_dernier_mesure(self):
                    date=""
                    for poid in PoidLapinProduction.objects.all():
                        if poid.lapin.groupe.id==self.id:
                                if date=="":
                                    date=poid.date_mesure
                                elif age(poid.date_mesure)<age(date):
                                    date=poid.date_mesure
                    return date
        # moyenne des poids des lapins des productions du groupe la dernier mesure
        def moyenne_poid_groupe_dernier_mesure(self):
                    moy=0
                    nb=0
                    for poid in PoidLapinProduction.objects.all():
                        if poid.lapin.groupe.id==self.id:
                                if poid.date_mesure==self.date_dernier_mesure():
                                    nb=nb+1
                                    moy=moy+poid.valeur
                    if nb!=0:
                        return int(moy/nb) 
                    else:
                        return "y'a pas des mesures" 
        # les dates de mesure des poids du groupe
        def dates_mesure_poids(self):
            dates=[]
            for poid in PoidLapinProduction.objects.all():
                            if poid.lapin.groupe.id==self.id:
                                    if not(str(poid.date_mesure) in dates):
                                        dates.append(str(poid.date_mesure))
            for i in range(len(dates)-1):
                    min=i
                    for j in range (i+1,len(dates)):
                        if age(dates[j])<age(dates[min]):
                            min=j
                    if age(dates[j])<age(dates[i]):
                            aux=dates[min]
                            dates[min]=dates[i]
                            dates[i]=aux
            return dates
        # moyenne des poids des lapins des productions du groupe a partir de son naissance
        def moyenne_poid_groupe_list(self):
                    dates=self.dates_mesure_poids()
                    moyenne_poids=[]
                    for date in dates:
                        print(date,age(date))
                        nb=0
                        totale=0
                        for poid in PoidLapinProduction.objects.all():
                            if poid.lapin.groupe.id==self.id:
                                    if str(poid.date_mesure)==date:
                                        nb=nb+1
                                        totale=totale+poid.valeur
                        
                        moyenne_poids.insert(
                            0,
                            {
                                "date":age(GroupeProduction.objects.get(id=self.id).date_naissance)-age(date),
                                "mesure":totale/nb,
                            })

                    return moyenne_poids   

        #nombre des malles ou des femalles dans le groupe 
        def nombre_malle_groupe(self):
                    nb=0
                    for lapin in LapinProduction.objects.filter(groupe=self):
                        if lapin.sex=="malle":
                                nb=nb+1
                    return nb             
        def nombre_femalle_groupe(self):
                    nb=0
                    for lapin in LapinProduction.objects.filter(groupe=self):
                        if lapin.sex=="femalle":
                                nb=nb+1
                    return nb   
        # calculer le taux des consomation du groupe entre deux date
        def cons_totale(self,initial_date,final_date):
            totale=0
            for date in list_dates(str(initial_date),str(final_date)):# pd.date_range(end=final_date,start=initial_date).tolist() :
                nb_lapin=GroupeProduction.objects.get(id=self.id).nb_lapins_nées
                # pour eleminer les lapins mortes avant ce date
                for lapin in LapinProduction.objects.filter(groupe=self.id):
                    if lapin.state=='mort':
                        if age(lapin.date_mort)>=age(date):
                            nb_lapin-=1
                if age(GroupeProduction.objects.get(id=self.id).date_naissance)-age(date)<25:
                    totale+=(0*nb_lapin)
                elif(age(GroupeProduction.objects.get(id=self.id).date_naissance)-age(date))< 30:
                    totale+=(5*nb_lapin)
                elif(age(GroupeProduction.objects.get(id=self.id).date_naissance)-age(date))< 44:
                    totale+=(50*nb_lapin)
                elif(age(GroupeProduction.objects.get(id=self.id).date_naissance)-age(date))< 59:
                    totale+=(100*nb_lapin)   
                elif(age(GroupeProduction.objects.get(id=self.id).date_naissance)-age(date))> 60:
                    totale+=(150*nb_lapin)
            return totale          
            
        def __str__(self):
            return str(self.cage)       
class LapinProduction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True)
    groupe=models.ForeignKey(GroupeProduction,on_delete=models.CASCADE,default=1)
    sex=models.CharField(max_length=50, default='non verifier',choices=[("femalle","femalle"),("malle","malle"),('non verifier','non verifier')])
    LAPIN_RACES=(
    ('Gaint Flander','Gaint Flander'),
    ('Flemish Giant','Flemish Giant'),
    ('Chinchilla','Chinchilla'),
    ('New Zealand White','New Zealand White'),
    ('California','California'),
    ('Rex','Rex')
    )
    race=models.ForeignKey(Race,on_delete=models.CASCADE,null=True ,blank=True)
    state=models.CharField(max_length=50, default='production',choices=[("mort","mort"),("vendue","vendue"),("production","production"),])
    cage=models.CharField(max_length=50,null=True,blank=True)
    #informations mort
    date_mort=models.DateField(null=True,blank=True)
    #informations vendue
    prix=models.IntegerField(null=True,blank=True)
    date_vent=models.DateField(null=True,blank=True)
    #le poid  du lapin  a la naissance
    def poid_naissance(self):
            for poid in PoidLapinProduction.objects.all():
                if poid.lapin.id==self.id:
                        if poid.date_mesure==poid.lapin.groupe.date_naissance:
                            return poid.valeur
            
            return "y'a pas des mesures"  
    # retourner la dernier date de mesure des poids du lapin
    def date_dernier_mesure(self):
                    date=""
                    for poid in PoidLapinProduction.objects.all():
                        if poid.lapin.id==self.id:
                                if date=="":
                                    date=poid.date_mesure
                                elif age(poid.date_mesure)<age(date):
                                    date=poid.date_mesure
                    return date
        
    #  poids du lapin du productions  la dernier mesure
    def poid_dernier_mesure(self):
                    for poid in PoidLapinProduction.objects.all():
                        if poid.lapin.id==self.id:
                                if poid.date_mesure==self.date_dernier_mesure():
                                    return poid.valeur
                    return "y'a pas des mesures" 
    # poid du lapin au sevrage
    def poid_sevrage(self):
        if self.groupe.date_souvrage!=None:  
            for poid in PoidLapinProduction.objects.all():      
                if poid.date_mesure==self.groupe.date_souvrage:
                    return poid.valeur
        return "y'a pas des mesure"            
    # les dates de mesure des poids du groupe
    def dates_mesure_poids(self):
            dates=[]
            for poid in PoidLapinProduction.objects.all():
                            if poid.lapin.id==self.id:
                                    if not(str(poid.date_mesure) in dates):
                                        dates.append(str(poid.date_mesure))
            # tri selection pour ordonné les date du age plus garnd au age plus petite
            for i in range(len(dates)-1):
                    min=i
                    for j in range (i+1,len(dates)):
                        if age(dates[j])<age(dates[min]):
                            min=j
                    if age(dates[j])<age(dates[i]):
                            aux=dates[min]
                            dates[min]=dates[i]
                            dates[i]=aux
            return dates
    # moyenne des poids des lapins des productions du groupe a partir de son naissance
    def poid_lapin_list(self):
                    dates=self.dates_mesure_poids()
                    poids=[]
                    for date in dates:
                        for poid in PoidLapinProduction.objects.filter(lapin=self.id):
                                    if str(poid.date_mesure)==date:
                                        poids.insert(
                            0,
                            {
                                "date":age(self.groupe.date_naissance)-age(date),
                                "mesure":poid.valeur,
                            })
                        
                        
                    return poids    
    def vaccins (self):
        vaccins=[]
        for vaccin in VaccinLapin.objects.filter(lapin=self.id):
            vaccins.append(
                                {
                                    "nom":str(vaccin.nom),
                                    "date_vaccin":str(age_handler(vaccin.date_vaccin)),
                                    "prix":str(vaccin.prix),
                                    "maladie":str(vaccin.maladie),
                                }
                            )    
        return vaccins           
    def __str__(self):
        return str(self.cage)
class PoidLapinProduction(models.Model):
    lapin=models.ForeignKey(LapinProduction,on_delete=models.CASCADE ,null=True , blank=True)
    date_mesure=models.DateField(null=True,blank=True)
    valeur=models.IntegerField(null=True,blank=True)
class VaccinLapin(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True)
    MALADIES_LAPINS=[('La gale', 'La gale'),
    ('La teigne' ,'La teigne'),
    ('Les mycoses' ,'Les mycoses'),
    ('La myxomatose' ,'La myxomatose'),
    ('Le coryza','Le coryza'),
    ]
    lapin=models.ForeignKey(LapinProduction,on_delete=models.CASCADE ,null=True , blank=True)
    date_vaccin=models.DateField(null=True,blank=True)
    nom=models.CharField(max_length=50,null=True,blank=True)
    prix=models.IntegerField(null=True,blank=True)
    maladie=models.CharField(choices=MALADIES_LAPINS ,max_length=200,default='non_vérifié')
    def __str__(self):
            return str(self.nom+" contre "+self.maladie)  




# la creation des nauveaux lapins a la creation d'un groupe
def create_lapin(sender,instance,created,**kwargs):
        if created:
                for i in range(int(instance.nb_lapins_mortes_naissances)):
                                LapinProduction.objects.create(
                                                        user=instance.user,
                                                        groupe=instance,                 
                                                        state='mort',
                                                        date_mort=instance.date_naissance,
                                                        
                                                        )              
                                                                                                                                                                
                for i in range(int(instance.nb_lapins_nées)-int(instance.nb_lapins_mortes_naissances)):
                                LapinProduction.objects.create(  
                                                        user=instance.user               ,     
                                                        groupe=instance,
                                                        cage='R'+str(i+1),
                                                        state='production',
                                                        )      
                   
               
post_save.connect(create_lapin,sender=GroupeProduction)