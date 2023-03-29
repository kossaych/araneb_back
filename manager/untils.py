# calculer l'age d'un lapin retourner le nombre de jour a partir du date de naissance (str!!) il retourne un entier
from datetime import date ,datetime
from django.utils import timezone
import pandas as pd


def age(naissance):
        """ naissance=str(naissance)
        année_naissance =int(naissance[:naissance.index('-')])
        month_naissance =int(naissance[naissance.index('-')+1:naissance.index('-',naissance.index('-')+1)])
        jour =int(naissance[naissance.index('-',naissance.index('-',naissance.index('-')+1))+1:])
        today = timezone.now() 
        nb_months=today.month-month_naissance # nombre des months
        jours_month=0 # le nombre des jours correspondant au nombre des months
        if nb_months>0:
            for month in range(month_naissance,today.month):
                if month in [1,3,5,7,8,10,12]:
                    jours_month=jours_month+31
                elif month in [4,6,5,9,8,10,11]  :
                    jours_month=jours_month+30
                else:    
                    if (année_naissance%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if année_naissance%400==0:
                                jours_month=jours_month+29
                            else:
                                jours_month=jours_month+28
                    else:
                            if année_naissance%4==0:
                                jours_month=jours_month+29
                            else:
                                jours_month=jours_month+28
        elif nb_months<0:
            for month in range(month_naissance,today.month,-1):
                if month in [1,3,5,7,8,10,12]:
                    jours_month=jours_month-31
                elif month in [4,6,5,9,8,10,11]  :
                    jours_month=jours_month-30
                else :
                    if (année_naissance%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                        if année_naissance%400==0:
                            jours_month=jours_month-29
                        else:
                            jours_month=jours_month-28
                    else:
                        if année_naissance%4==0:
                            jours_month=jours_month-29
                        else:
                            jours_month=jours_month-28
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
        age = jours_anné+jours_month+ (today.day - jour)
        return  age """
        str_d1 = str(naissance)
        aujourdhui_date=str(date.today())
        
        try:
            d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        except:
            str_d1 = str_d1[:str_d1.find(" ")] # sa por séparer le date et l'heure
            d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(aujourdhui_date, "%Y-%m-%d")
        age = str(d2 - d1)
        try :    
            age=int(age[:age.index('d')])
        except:
            age=0
        return  age
# retourner l'age en anné months et jours sous forme str a partir du date de naissance
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
                    #nb_months=age


                    nb_months=0
                    while (age>=30):
                        if today.month-nb_months in [1,3,5,7,8,10,12]:
                            age-=31
                        elif today.month-nb_months in [4,6,5,9,8,10,11]  :
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
                        nb_months+=1        
                    
                return str(nb_anné)+" ans "+str(nb_months)+" months "+str(age)+" jours "  
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
    #print('dates',initial_date,final_date)
    list_dates= pd.date_range(start=initial_date, end=final_date)
    """ list_dates=[]
    initial_date=datetime.strptime(initial_date, "%Y-%m-%d")
    final_date=datetime.strptime(final_date, "%Y-%m-%d")
    initial_year=int(initial_date.year)
    final_year=int(final_date.year)
    for year in range(initial_year,final_year+1):
            print('y',year)
            initial_month=1
            final_month=12
            if year == final_year :
                final_month=final_date.month
            if year == initial_year:
                initial_month=initial_date.month
                 
            for month in range(initial_month,final_month+1):
                print('m',month)
                if month in [4,6,9,11]:
                                initial_day =1
                                final_day = 30
                                if year == final_year and month == final_month  :
                                    final_day =final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 

                                for jour in range(initial_day,final_day+1):
                                    print('j',jour)
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    
                                    if month in [4,6,9]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)

                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    list_dates.append(date)
                                    
                elif month in [1,3,5,7,8,10,12]:   
                                initial_day =1
                                final_day = 31
                                if year == final_year and month == final_month  :
                                    final_day =final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    print('j',jour)
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    if month in [1,3,5,7,8]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
                                    
                if month == 2 :
                    if (year %1000)%100==0:  # si le disaine et l'unité de l'nannée  est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if year % 400 == 0:
                                initial_day =1
                                final_day = 29
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    print('j',jour)
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
                                    
                            else:
                                initial_day =1
                                final_day = 28
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    print('j',jour)
                                    month_date=str(month)
                                    jour_date=str(jour)
                                     
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
                                    
                    else:
                            if year %4==0:
                                initial_day =1
                                final_day = 29
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    print('j',jour)
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    list_dates.append(date)                                    
                                                                
                                    
                            else:
                                initial_day =1
                                final_day = 28
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    print('j',jour)
                                    month_date=str(month)
                                    jour_date=str(jour)
                                     
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    list_dates.append(date)         

    """ 
    #print(list_dates)             
    return list_dates
    #naissance a partir d'un age par jour
def age_revers(age_jours):
        if age_jours >= 364 :
            for an in range((timezone.now().year-(age_jours//365))-1,(timezone.now().year-(age_jours//365))+1):
                for month in range(1,13):                       
                                if month in [4,6,9,11]:
                                                for jour in range(1,31):
                                                    if age(str(an)+"-"+str(month)+"-"+str(jour)) == age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                                
                                elif month in [1,3,5,7,8,10,12]:   
                                                for jour in range(1,32):
                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                                                              
                                if month == 2 :
                                    if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                            if an%400==0:
                                                for jour in range(1,30):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                              
                                            else:
                                                for jour in range(1,29):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                               
                                    else:
                                            if an%4==0:
                                                for jour in range(1,30):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                            
                                            else:
                                                for jour in range(1,29):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                     
        else:      
            if (int(age(str(timezone.now().year)+"-01-01"))>=age_jours):#pour assurer que les dates doit  etre dans cette anné
                    an = timezone.now().year   
            else:
                    an = timezone.now().year-1                   
            for month in range(1,13):                       
                            if month in [4,6,9,11]:
                                            for jour in range(1,31):
                                                if age(str(an)+"-"+str(month)+"-"+str(jour)) == age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                                
                            elif month in [1,3,5,7,8,10,12]:   
                                            for jour in range(1,32):
                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                                                              
                            if month == 2 :
                                if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                        if an%400==0:
                                            for jour in range(1,30):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                              
                                        else:
                                            for jour in range(1,29):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                               
                                else:
                                        if an%4==0:
                                            for jour in range(1,30):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                            
                                        else:
                                            for jour in range(1,29):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                     
