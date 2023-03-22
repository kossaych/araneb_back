# calculer l'age d'un lapin retourner le nombre de jour a partir du date de naissance (str!!) il retourne un entier
from datetime import date ,datetime
from django.utils import timezone

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
        """today=timezone.now()
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
